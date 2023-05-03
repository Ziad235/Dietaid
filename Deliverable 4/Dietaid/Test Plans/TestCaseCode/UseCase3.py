#  test cases using django test framework

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import doctor, patient, User
from django.urls import reverse
from .models import Diagnosis, Patient, Doctor, Diet, Meal, MealPlan, MealPlanDiet, MealPlanMeal, MealPlanPatient, MealPlanDoctor, MealPlanDiagnosis, MealPlanMealPlan
from .forms import DiagnosisForm, PatientForm, DoctorForm, DietForm, MealForm, MealPlanForm, MealPlanDietForm, MealPlanMealForm, MealPlanPatientForm, MealPlanDoctorForm, MealPlanDiagnosisForm, MealPlanMealPlanForm

#  test case for The doctor logs in to the platform, navigates to the patient's profile, selects the "View meal-plan" option, reviews the meal-plan details, makes any necessary edits, and approves the meal-plan. The patient is now able to see the approved meal-plan
class TestApproveMealPlan(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_approve_mealplan(self):
        response = self.client.get('/patient/1/mealplan/approve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
    
    def test_approve_mealplan_success(self):
        response = self.client.get('/patient/1/mealplan/approve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/approve/', {'mealplan': 'test', 'mealplan_date': '2019-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/patient/1/')
        response = self.client.get('/patient/1/')
        self.assertContains(response, 'test')

#  test case for The doctor accidentally approves the wrong meal-plan for the patient. The patient notifies the doctor of the error, and the doctor edits or deletes the meal-plan.
class TestEditMealPlan(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_edit_mealplan(self):
        response = self.client.get('/patient/1/mealplan/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
    
    def test_edit_mealplan_success(self):
        response = self.client.get('/patient/1/mealplan/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/edit/', {'mealplan': 'test', 'mealplan_date': '2019-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/patient/1/')
        response = self.client.get('/patient/1/')
        self.assertContains(response, 'test')

#  test case for The doctor tries to edit or approve a meal-plan that has already been approved. The platform displays an error message and does not allow the action to be taken.
class TestEditApprovedMealPlan(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_edit_approved_mealplan(self):
        response = self.client.get('/patient/1/mealplan/approve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
    
    def test_edit_approved_mealplan_success(self):
        response = self.client.get('/patient/1/mealplan/approve/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/approve/', {'mealplan': 'test', 'mealplan_date': '2019-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/patient/1/')
        response = self.client.get('/patient/1/')
        self.assertContains(response, 'test')
        response = self.client.get('/patient/1/mealplan/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mealplan_form.html')
        response = self.client.post('/patient/1/mealplan/edit/', {'mealplan': 'test2', 'mealplan_date': '2019-12-12'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/patient/1/')
        response = self.client.get('/patient/1/')
        self.assertContains(response, 'test')
        