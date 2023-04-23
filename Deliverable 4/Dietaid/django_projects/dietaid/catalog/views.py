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

def is_doctor(user):
    if(user.groups.filter(name='Doctor').exists()):
        return True
    else:
        return False



# decorator to require login before seeing the page
@login_required
def index(request):
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



def create_diagnosis(request):

    patient = get_object_or_404(User, pk=request.GET.get('user_pk'))

    if request.method == 'POST':

        form = DiagnosisForm(request.POST)
        if form.is_valid():
            diagnosis_choice = request.POST.get("diagnosis_summary")#form.diagnosis_summary
            diagnosis_notes = request.POST.get("notes") #form.notes
            new_diagnosis = Diagnosis(patient_id = patient.id, doctor_id = request.user.id, summary = diagnosis_choice, notes = diagnosis_notes)
            new_diagnosis.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = DiagnosisForm()
        context = {
            'form': form,
            'patient_name': patient.first_name + " " + patient.last_name, 
        }
        return render(request, 'catalog/create_diagnosis_form.html', context)


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


def generate_mealplan(request):
    diagnosis = get_object_or_404(Diagnosis, id = request.GET.get('diagnosis_id'))
    print(diagnosis)
    if request.method == 'POST':
        form = MealplanPreferenceForm(request.POST)
        if form.is_valid():
            preference = request.POST.get("preference")
            new_mealplan = Mealplan()
            new_mealplan.preference = preference
            new_mealplan.breakfast = MEALPLAN_MAPPER[diagnosis.summary]['breakfast'][preference]
            new_mealplan.lunch = MEALPLAN_MAPPER[diagnosis.summary]['lunch'][preference]
            new_mealplan.dinner = MEALPLAN_MAPPER[diagnosis.summary]['dinner'][preference]
            new_mealplan.doctor_id = diagnosis.doctor_id
            new_mealplan.patient_id = diagnosis.patient_id
            new_mealplan.diagnosis_id = diagnosis.id
            new_mealplan.save()
            return HttpResponseRedirect(reverse('index'))
    else: 
        form = MealplanPreferenceForm()
        context = {
            'form': form,
        }
        return render(request, 'catalog/mealplan_preference_form.html', context)


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

def edit_mealplan(request):
    mealplan = get_object_or_404(Mealplan, pk = request.GET.get('mealplan_id'))
    patient = get_object_or_404(User, pk = mealplan.patient_id)
    #patient = User.objects.filter(id__exact = mealplan.patient_id)
    #doctor = User.objects.filter(id__exact = mealplan.doctor_id)

    if request.method == 'POST':
        form = MealplanEditForm(request.POST, instance = mealplan)
        if form.is_valid():
            form.save()
            mealplan.approved = True
            mealplan.save()
            return HttpResponseRedirect(reverse('index'))
    
    else:
        form = MealplanEditForm(instance=mealplan)
        context = {
            'form':form,
            'patient_name': patient.first_name + " " + patient.last_name, 
        }
        return render(request, 'catalog/edit_mealplan.html', context)



            





@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)