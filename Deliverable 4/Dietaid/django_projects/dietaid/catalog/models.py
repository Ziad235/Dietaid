from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User

from datetime import date

class UserProfile(models.Model):
    role = models.CharField(max_length=10) # patient, doctor, or admin
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    BMI = models.FloatField()
    body_fat_percentage = models.FloatField()
    medical_history = models.CharField(max_length=500)


# Create models here.
class Mealplan(models.Model):
    patient_id = models.IntegerField()
    patient_lastname = models.CharField(max_length = 100)

    doctor_id = models.IntegerField()
    doctor_lastname = models.CharField(max_length = 100)

    diagnosis_id = models.IntegerField()
    
    preference = models.CharField(max_length = 500)
    allergy = models.CharField(max_length = 50)

    breakfast = models.CharField(max_length = 500)
    lunch = models.CharField(max_length = 500)
    dinner = models.CharField(max_length = 500)

    notes_from_doctor = models.CharField(max_length = 500)

    approved = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Diagnosis(models.Model):
    # since both patients and doctors use the default user class, this is to avoid clashes
    patient_id = models.IntegerField()
    patient_lastname = models.CharField(max_length = 100)

    doctor_id = models.IntegerField()
    doctor_lastname = models.CharField(max_length = 100)
   
    description = models.CharField(max_length=500)
    summary = models.CharField(max_length = 100)
    notes = models.CharField(max_length = 300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# The following are classes from the tutorials
# =============================================
