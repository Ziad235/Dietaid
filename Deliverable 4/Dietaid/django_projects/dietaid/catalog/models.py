from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

"""
class Patient(models.Model):
    # Model representing an patient.
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        #Returns the URL to access a particular author instance.
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        #String for representing the Model object.
        return f'{self.last_name}, {self.first_name}'
"""

class Mealplan(models.Model):
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
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
    doctor_id = models.IntegerField()
   
    summary = models.CharField(max_length = 100)
    notes = models.CharField(max_length = 300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# The following are classes from the tutorials
# =============================================
