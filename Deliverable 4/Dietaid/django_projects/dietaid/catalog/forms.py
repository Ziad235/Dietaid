import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Mealplan

"""
DIAGNOSIS_CHOICES = [
    ("1", "IBS"),
    ("2", "Fatty liver"),
    ("3", "High blood pressure"), 
    ("4", "PCOS"),
    ("5", "Heart health"),
    ("6", "Diabetes"),
    ("7", "Hypothyroidism"),
    ("8", "Overweight/obesity"),
    ("9", "High cholesterol"), 
    ("10", "Hashimoto’s"),
    ("11", "Menopause"),
    ("12", "Diverticulitis"),
    ("13", "Inflammation"),
    ("14", "Arthritis"), 
    ("15", "GERD")
]
"""

DIAGNOSIS_CHOICES = [
    ("IBS", "IBS"),
    ("Fatty liver", "Fatty liver"),
    ("High blood pressure", "High blood pressure"), 
    ("PCOS", "PCOS"),
    ("Heart health", "Heart health"),
    ("Diabetes", "Diabetes"),
    ("Hypothyroidism", "Hypothyroidism"),
    ("Overweight/obesity", "Overweight/obesity"),
    ("High cholesterol", "High cholesterol"), 
    ("Hashimoto’s", "Hashimoto’s"),
    ("Menopause", "Menopause"),
    ( "Diverticulitis", "Diverticulitis"),
    ("Inflammation", "Inflammation"),
    ("Arthritis", "Arthritis"), 
    ("GERD", "GERD")
]

PREFERECE_CHOICES = [
    ("None", "None"),
    ("Vegetarian", "Vegetarian"), 
    ("Vegan", "Vegan"), 
    ("Pescatarian", "Pescatarian"), 
]


class DiagnosisForm(forms.Form):
    diagnosis_summary= forms.MultipleChoiceField(choices = DIAGNOSIS_CHOICES)
    notes = forms.CharField(widget=forms.Textarea)

class MealplanPreferenceForm(forms.Form):
    preference = forms.MultipleChoiceField(choices=PREFERECE_CHOICES) #widget=forms.CheckboxSelectMultiple()
    allergy = forms.CharField(help_text="Enter the allergy you have. ")

class MealplanEditForm(forms.ModelForm):
    class Meta:
        model = Mealplan
        fields = [
            'breakfast',
            'lunch',
            'dinner',
            'notes_from_doctor',
        ]
