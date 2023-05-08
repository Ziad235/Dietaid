from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

 
 
def doctor_test_function(user):
    if user.userprofile.role == "doctor":
        return True
    return False

def doctor_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not doctor_test_function(request.user):
                return HttpResponseRedirect(reverse('not-authorized'))
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator