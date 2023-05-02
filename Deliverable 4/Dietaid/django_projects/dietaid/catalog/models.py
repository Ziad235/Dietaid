from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date

# Create models here.
class Mealplan(models.Model):
    patient_id = models.IntegerField()
    patient_lastname = models.CharField(max_length = 100)

    doctor_id = models.IntegerField()
    doctor_lastname = models.CharField(max_length = 100)

    diagnosis_id = models.IntegerField()
    
    preference = models.CharField(max_length = 500)

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
   
    summary = models.CharField(max_length = 100)
    notes = models.CharField(max_length = 300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# The following are classes from the tutorials
# =============================================
