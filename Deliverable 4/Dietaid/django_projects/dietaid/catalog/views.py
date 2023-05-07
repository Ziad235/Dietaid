from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Import model
from .models import Diagnosis, Mealplan
import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from .meal_plan_config import MEALPLAN_MAPPER


### inmport new form here
from catalog.forms import DiagnosisForm, MealplanPreferenceForm, MealplanEditForm

#=====================
# check if the logged in user is doctor or patient
def is_doctor(user):
    if(user.groups.filter(name='Doctor').exists()):
        return True
    else:
        return False
def is_patient(user):
    if(user.groups.filter(name='Patient').exists()):
        return True
    else:
        return False



# decorator to require login before seeing the page
@login_required
def index(request):
    if(request.user.groups.filter(name='Admin').exists()):
        return HttpResponseRedirect(reverse('admin:index'))

    #View function for home page of site.
    all_patients = User.objects.filter(groups__name__in = ['Patient'])
    all_diagnosis = Diagnosis.objects.filter(patient_id__exact = request.user.id).order_by('-created_at')
    my_mealplans = Mealplan.objects.filter(patient_id__exact = request.user.id).order_by('-created_at')

    if(is_doctor(request.user)):
        my_mealplans = Mealplan.objects.filter(doctor_id__exact = request.user.id).order_by('-created_at')
    
    context = {
        'patient_list': all_patients,
        'diagnosis_list': all_diagnosis,
        'is_doctor': is_doctor(request.user),
        'mealplan_list': my_mealplans,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# form to create the diagnosis
@login_required
def create_diagnosis(request):

    patient = get_object_or_404(User, pk=request.GET.get('user_pk'))

    if request.method == 'POST':

        form = DiagnosisForm(request.POST)
        if form.is_valid():
            diagnosis_description = request.POST.get("diagnosis_description")
            diagnosis_choice = request.POST.get("diagnosis_summary")#form.diagnosis_summary
            diagnosis_notes = request.POST.get("notes") #form.notes

            new_diagnosis = Diagnosis()
            new_diagnosis.patient_id = patient.id
            new_diagnosis.patient_lastname = patient.last_name

            new_diagnosis.doctor_id = request.user.id
            new_diagnosis.doctor_lastname = request.user.last_name

            new_diagnosis.description = diagnosis_description
            new_diagnosis.summary = diagnosis_choice
            new_diagnosis.notes = diagnosis_notes
            
            new_diagnosis.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = DiagnosisForm()
        context = {
            'form': form,
            'patient_name': patient.first_name + " " + patient.last_name, 
        }
        return render(request, 'catalog/create_diagnosis_form.html', context)

@login_required
def diagnosis_detail_view(request):
    diagnosis = get_object_or_404(Diagnosis, pk = request.GET.get('diagnosis_id'))

    patient = User.objects.filter(id__exact = diagnosis.patient_id)
    doctor = User.objects.filter(id__exact = diagnosis.doctor_id)
    context = {
        'diagnosis': diagnosis,
        'patient': patient,
        'doctor': doctor,
    }
    return render(request, 'catalog/diagnosis_detail.html', context)

# form to generate the mealplan
@login_required
def generate_mealplan(request):
    diagnosis = get_object_or_404(Diagnosis, id = request.GET.get('diagnosis_id'))
    
    doctor = get_object_or_404(User, pk=diagnosis.doctor_id)
    patient = get_object_or_404(User, pk=diagnosis.patient_id)

    # store the form
    if request.method == 'POST':
        form = MealplanPreferenceForm(request.POST)
        if form.is_valid():
            preference = request.POST.get("preference")
            allergy = request.POST.get("allergy")
            new_mealplan = Mealplan()
            new_mealplan.preference = preference
            new_mealplan.allergy = allergy
            new_mealplan.breakfast = MEALPLAN_MAPPER[diagnosis.summary]['breakfast'][preference]
            new_mealplan.lunch = MEALPLAN_MAPPER[diagnosis.summary]['lunch'][preference]
            new_mealplan.dinner = MEALPLAN_MAPPER[diagnosis.summary]['dinner'][preference]
            new_mealplan.doctor_id = diagnosis.doctor_id
            new_mealplan.doctor_lastname = doctor.last_name
            new_mealplan.patient_id = diagnosis.patient_id
            new_mealplan.patient_lastname = patient.last_name
            new_mealplan.diagnosis_id = diagnosis.id
            new_mealplan.save()
            return HttpResponseRedirect(reverse('index'))
    else: # render the form 
        form = MealplanPreferenceForm()
        context = {
            'form': form,
        }
        return render(request, 'catalog/mealplan_preference_form.html', context)

# render mealplan details
@login_required
def mealplan_detail_view(request):
    mealplan = get_object_or_404(Mealplan, pk = request.GET.get('mealplan_id'))
    patient = get_object_or_404(User, pk = mealplan.patient_id)
    doctor = get_object_or_404(User, pk = mealplan.doctor_id)

    context = {
        'diagnosis': mealplan,
        'patient': patient,
        'doctor': doctor,
        'mealplan': mealplan,
        'is_doctor': is_doctor(request.user),
    }
    return render(request, 'catalog/mealplan_detail.html', context)

@login_required
def patient_profile(request):
    
    patient = get_object_or_404(User, pk = request.GET.get('patient_id'))
    diagnosis_list = Diagnosis.objects.filter(patient_id__exact = patient.id).order_by('-created_at')
    mealplan_list = Mealplan.objects.filter(patient_id__exact = patient.id).order_by('-created_at')

    context = {
        "patient": patient,
        "diagnosis_list": diagnosis_list,
        "mealplan_list": mealplan_list,
    }
    return render(request, 'catalog/patient_profile.html', context)

# form to edit meal plan
@login_required
def edit_mealplan(request):
    mealplan = get_object_or_404(Mealplan, pk = request.GET.get('mealplan_id'))
    patient = get_object_or_404(User, pk = mealplan.patient_id)

    # to submit form 
    if request.method == 'POST':
        form = MealplanEditForm(request.POST, instance = mealplan)
        if form.is_valid():
            form.save()
            mealplan.approved = True
            mealplan.save()
            return HttpResponseRedirect(reverse('index'))
    
    # to render form
    else:
        form = MealplanEditForm(instance=mealplan)
        context = {
            'form':form,
            'mealplan': mealplan,
            'patient_name': patient.first_name + " " + patient.last_name, 
            'patient': patient
        }
        return render(request, 'catalog/edit_mealplan.html', context)

@login_required
def search_patients(request):
    context = {
        "is_doctor": True,
        "patients": [],
    }
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        if patient_name == "":
            return render(request, 'catalog/search_patients.html', context)
        
        found_patients = User.objects.filter(first_name__startswith = patient_name)
        context["patients"] = []

        # only include patients in teh system
        for p in found_patients:
            if is_patient(p):
                context['patients'].append(p)

        return render(request, 'catalog/search_patients.html', context)

    else: 
        return render(request, 'catalog/search_patients.html', context)


        