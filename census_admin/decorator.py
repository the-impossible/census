# My django imports
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages

# My app imports
# from bot_authentication.decorator import has_paid


def is_staff(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return func(request, *args, **kwargs)
            else:
                return redirect('auth:dashboard')         
    return wrapper_func