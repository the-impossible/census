# My django imports
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
import datetime

# My app imports
from bot.models import PaymentDetails
from census_admin.models import Accounts

def allowed_users(allowed_group=[]):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_group:
                    return wrapper_func(request, *args, **kwargs)
                else:
                    return render(request, 'unauthorize.html')
            else:
                return render(request, 'unauthorize.html')
        else:
            messages.error(request, 'You are not authorized to view that page')
            return render(request, 'authentication/account.html')
    return wrapper_func

def authenticated_user(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in, Try logging out first!')
            return redirect('auth:dashboard')
        else:
            return func(request, *args, **kwargs)
    return wrapper_func


def only_authenticated_users(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            messages.warning(request, 'You can not logout when you are not logged in!')
            return redirect('users:home')
    return wrapper_func
