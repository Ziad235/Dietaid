from django.contrib import admin

# Register your models here.

from .models import Mealplan, Diagnosis

admin.site.register(Diagnosis)
admin.site.register(Mealplan)

