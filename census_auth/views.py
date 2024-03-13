# My django imports
from random import choice, randint, shuffle, randrange
from django.contrib import messages #for sending messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout #authentication
import json
from validate_email import validate_email #for validating email address
from django.http.response import JsonResponse #returning ajax request
from django.contrib.auth.mixins import LoginRequiredMixin

# My app imports
from census_auth.forms import RegistrationForm
from census_auth.models import Accounts
from census_users.models import UserProfile

# Create your views here.
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username'].lower()
        if Accounts.objects.filter(username=username).exists():
            return JsonResponse(
                {'username_error':'Username already taken'}, status=406
            )
            
        else:
            return JsonResponse(
            {'username_valid':'True'}, status=200
            )
            

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email'].lower()        
        
        if not validate_email(email):
            return JsonResponse(
                {'email_error': 'Invalid Email'}, status=400
            )
        if Accounts.objects.filter(email=email).exists():
            return JsonResponse(
                {'email_error':'Email already taken'}, status=400
            )
        return JsonResponse(
            {'email_valid':'True'}, status=200
        )
        
            
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'You are still logged in')
            if request.user.is_staff:
                return redirect('staff:admin_dashboard')
            else:
                return redirect('auth:dashboard')
                
        else:
            context = {}
            return render(request, 'auth/login.html', context)
    
    def post(self, request):
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        if username and password:
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user:
                if user.is_active:
                    login(request, user)
                    if user.is_staff:
                        messages.success(request, 'You are now logged in')
                        return redirect('staff:admin_dashboard')
                    else:
                        messages.success(request, 'You are now logged in!')
                        return redirect('auth:dashboard')
                else:
                    messages.warning(request, 'Account not active contact the administrator')
                    return redirect('auth:login')
            else:
                messages.warning(request, 'Invalid login credentials')
                return render(request, 'auth/login.html', {'username':username})
            
        elif request.user.is_authenticated:
            messages.info(request, 'You are already login')
            
            if request.user.is_staff:
                
                return redirect('staff:admin_dashboard')
            else:
                return redirect('auth:dashboard')
        else:
            messages.error(request, f'Please fill in all empty field')
            return redirect('auth:login')
    

class LogoutView(View):
    
    def get(self, request):        
        try:
            logout(request)
            messages.success(request, 'You are now logged out')
        except:
            pass    
        return redirect('users:home')


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'You are still logged in')
            if request.user.is_staff:
                return redirect('staff:admin_dashboard')
            else:
                return redirect('auth:dashboard')
                
        else:            
            context = {
                'form':RegistrationForm
            }
            return render(request, 'auth/register.html', context)
    
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        
        def generate_id():
            id = 'CBCIM0'+ str(randint(80, 1000))
            found = Accounts.objects.filter(acct_id=id)
            if found:
                generate_id()
                
            return id
        
        if form.is_valid():
            user = form.save(commit=False)
            # data's to be saved
            try:
                username = int(user.username)
            except:
                messages.error(request, (f'form error'))
                return render(request, 'auth/register.html', {'form':form}) 
            
            
            # data's to be saved
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.set_password(user.password)
            user.acct_id = generate_id()
            user.save()
            
            messages.success(request, (f'{username} your account is created You can now login'))
            return redirect('users:home')
            
        else:
            return render(request, 'auth/register.html', {'form':form}) 
        
        
class DashboardView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        try:
            profile = UserProfile.objects.get(user_id=request.user.id)
            if profile:
                
                lga_pop = UserProfile.objects.filter(lga=profile.lga).count()
                
                context = {
                'user':request.user,
                'status':True,
                'lga_pop':lga_pop,
                'profile':profile, 
            }
        except:
            context = {
                'user':request.user,
                'status':False    
            }
            
        return render(request, 'auth/dashboard.html', context)
    
    
