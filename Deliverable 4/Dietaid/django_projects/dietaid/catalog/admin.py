from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Mealplan, Diagnosis, UserProfile

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "userprofile"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Diagnosis)
admin.site.register(Mealplan)

