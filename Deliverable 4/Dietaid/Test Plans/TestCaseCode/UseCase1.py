# test cases using django test framework

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import doctor, patient, User
from django.urls import reverse
from .models import Diagnosis, Patient, Doctor, Diet, Meal, MealPlan, MealPlanDiet, MealPlanMeal, MealPlanPatient, MealPlanDoctor, MealPlanDiagnosis, MealPlanMealPlan
from .forms import DiagnosisForm, PatientForm, DoctorForm, DietForm, MealForm, MealPlanForm, MealPlanDietForm, MealPlanMealForm, MealPlanPatientForm, MealPlanDoctorForm, MealPlanDiagnosisForm, MealPlanMealPlanForm




# test case for the doctor logs in to the platform, navigates to the patient's profile, selects the "Create diagnosis" option, enters the diagnosis details, and saves it. The diagnosis is now added to the patient's profile and can be used for generating a meal-plan
class TestCreateDiagnosis(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_create_diagnosis(self):
        response = self.client.get('/patient/1/diagnosis/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')

# test case The doctor forgets to fill in a required field in the diagnosis form and tries to save it. The platform displays an error message and highlights the missing field.
    def test_create_diagnosis_missing_field(self):
        response = self.client.get('/patient/1/diagnosis/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        response = self.client.post('/patient/1/diagnosis/create/', {'diagnosis': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        self.assertContains(response, 'This field is required.')

#  test case The doctor fills in all the required fields in the diagnosis form and saves it. The platform displays a success message and redirects the doctor to the patient's profile page.
    def test_create_diagnosis_success(self):
        response = self.client.get('/patient/1/diagnosis/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        response = self.client.post('/patient/1/diagnosis/create/', {'diagnosis': 'test', 'diagnosis_date': '2019-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/patient/1/')
        response = self.client.get('/patient/1/')
        self.assertContains(response, 'test')

#  test case for The doctor accidentally selects the wrong diagnosis type from a drop-down menu and saves it. The diagnosis is now incorrect and needs to be edited or deleted.
    def test_create_diagnosis_wrong_diagnosis_type(self):
        response = self.client.get('/patient/1/diagnosis/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        response = self.client.post('/patient/1/diagnosis/create/', {'diagnosis': 'test', 'diagnosis_date': '2019-12-12', 'diagnosis_type': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        self.assertContains(response, 'Select a valid choice. 1 is not one of the available choices.')

#  test case for The doctor exceeds character/word limit in required field for diagnosis (300 word limit)
    def test_create_diagnosis_exceed_word_limit(self):
        response = self.client.get('/patient/1/diagnosis/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        response = self.client.post('/patient/1/diagnosis/create/', {'diagnosis': 'test' * 100, 'diagnosis_date': '2019-12-12'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diagnosis_form.html')
        self.assertContains(response, 'Ensure this value has at most 300 characters (it has 400).')


