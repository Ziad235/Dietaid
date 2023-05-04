#  test cases using django test framework

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import doctor, patient, User
from django.urls import reverse
from .models import Diagnosis, Patient, Doctor, Diet, Meal, MealPlan, MealPlanDiet, MealPlanMeal, MealPlanPatient, MealPlanDoctor, MealPlanDiagnosis, MealPlanMealPlan
from .forms import DiagnosisForm, PatientForm, DoctorForm, DietForm, MealForm, MealPlanForm, MealPlanDietForm, MealPlanMealForm, MealPlanPatientForm, MealPlanDoctorForm, MealPlanDiagnosisForm, MealPlanMealPlanForm

#  test case for The patient logs in to the platform, navigates to their profile, selects the "Request meal-plan" option, selects the diagnosis for which they want a meal-plan to be generated, and submits the request. The platform generates a meal-plan based on the patient's preferences and nutritional requirements, and displays it to the patient.
class TestRequestMealPlan(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_request_mealplan(self):
        response = self.client.get('/patient/1/mealplan/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')

#  test case for The patient forgets to fill in a required field in the meal-plan request form and tries to submit it. The platform displays an error message and highlights the missing field.
    def test_request_mealplan_missing_field(self):
        response = self.client.get('/patient/1/mealplan/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/request/', {'mealplan': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        self.assertContains(response, 'This field is required.')

#  test case for The patient forgets to select a diagnosis and submits the request. The platform displays an error message and prompts the patient to select a diagnosis.
    def test_request_mealplan_missing_diagnosis(self):
        response = self.client.get('/patient/1/mealplan/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/request/', {'mealplan': 'test', 'diagnosis': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        self.assertContains(response, 'This field is required.')

#  test case for The patient fills in the meal-plan request form and submits it. The platform generates a meal-plan based on the patient's preferences and nutritional requirements, and displays it to the patient.
    def test_request_mealplan_success(self):
        response = self.client.get('/patient/1/mealplan/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/request/', {'mealplan': 'test', 'diagnosis': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        self.assertContains(response, 'Meal Plan Requested')

#  test case for The patient selects a diagnosis that does not exist in the database. The platform displays an error message and prompts the patient to select a valid diagnosis.
    def test_request_mealplan_invalid_diagnosis(self):
        response = self.client.get('/patient/1/mealplan/request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/request/', {'mealplan': 'test', 'diagnosis': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        self.assertContains(response, 'Select a valid choice. test is not one of the available choices.')

    