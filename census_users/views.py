# My django imports
from random import randint
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages #for sending messages
from django.contrib.auth import authenticate #authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

# My app imports
from census_users.forms import UserProfileForm
from census_admin.models import LGA
from census_auth.forms import RegistrationForm
from census_auth.models import Accounts
from census_users.models import UserProfile, ContactSupport


# Create your views here.
class HomeView(View):
    def get(self, request):
        
        context = {
        }
        return render(request, 'users/index.html', context)
    

class AboutView(View):
    def get(self, request):
        
        context = {
        }
        return render(request, 'users/about.html', context)
    
class ContactView(View):
    def get(self, request):
        
        context = {
        }
        return render(request, 'users/contact.html', context)
    
    def post(self, request):
        fullname =  request.POST.get('fullname')
        email =  request.POST.get('email')
        message = request.POST.get('message')
        ContactSupport.objects.create(name=fullname, email=email, message=message)
        messages.success(request, 'Message sent, CBCIMS will contact you!')
        return render(request, 'users/contact.html')

class UserProfileView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        
        if request.user.is_staff:
            form = UserProfileForm()
            form2 = RegistrationForm()
            context = {
                'form':form,
                'form2':form2,
            }
        else:
            try:
                form = UserProfileForm(instance=request.user.profile)
            except:
                form = UserProfileForm()
            
            context = {
                'form':form,
            }
            
        return render(request, 'admin/create_users.html', context)
    
    def post(self, request):
        
        form = UserProfileForm(request.POST, request.FILES)
        form2 = RegistrationForm(request.POST)
        
        def generate_id():
            id = 'CBCIM0' + str(randint(80, 1000))
            found = Accounts.objects.filter(acct_id=id)
            if found:
                generate_id()
                
            return id
        
        if form.is_valid():
            profile_pic = form.cleaned_data.get('profile_pic')
            lastName = form.cleaned_data.get('lastName')
            firstName = form.cleaned_data.get('firstName')
            otherName = form.cleaned_data.get('otherName')
            address = form.cleaned_data.get('address')
            phoneNumber = form.cleaned_data.get('phoneNumber')
            gender = form.cleaned_data.get('gender')
            religion = form.cleaned_data.get('religion')
            lga = form.cleaned_data.get('lga')
            family_size = form.cleaned_data.get('family_size')
            dob = form.cleaned_data.get('dob')
            

            if 'username' in request.POST:
                if form2.is_valid():
                    user = form2.save(commit=False)
                    try:
                        user.username = int(user.username)
                    except:
                        messages.error(request, f'Value is required for NIN!')
                        
                        context = {
                            'form':form,
                            'form2':form2,
                        }
                        
                        return render(request, 'admin/create_users.html', context)
                    
                    user.email = user.email.lower()
                    user.acct_id = generate_id()
                    user.set_password(user.password)
                    user.save()
                    
                    profile = form.save(commit=False)
                    profile.user = user
                    
                    lga = LGA.objects.get(lga=lga)
                    lga.population += 1
                    lga.save()
                    
                    profile.save()
                    messages.success(request, f'User has been created!')
                
                    context = {
                        'form':UserProfileForm(),
                        'form2':RegistrationForm(),
                    }
                
                return render(request, 'admin/create_users.html', context)
                
            else:
                entry = UserProfile.objects.filter(user_id=request.user.id).exists()

                if entry:
                    print('user has profile')
                    profile_update = UserProfile.objects.get(user_id=request.user.id)
                    
                    if profile_pic !=None:
                        profile_update.profile_pic = profile_pic
                        
                    if lastName !=None:
                        profile_update.lastName = lastName
                        
                    if firstName !=None:
                        profile_update.firstName = firstName
                        
                    if otherName !=None:
                        profile_update.otherName = otherName
                        
                    if address !=None:
                        profile_update.address = address
                        
                    if phoneNumber !=None:
                        profile_update.phoneNumber = phoneNumber
                    
                    if gender !=None:
                        profile_update.gender = gender
                        
                    if religion !=None:
                        profile_update.religion = religion
                    
                    if lga !=None:
                        new = profile_update.lga
                        profile_update.lga = lga
                        
                        if profile_update.lga != lga:
                            print(profile_update.lga)
                            print(lga)
                            lga = LGA.objects.get(lga=lga)
                            lga.population += 1
                            print(lga.population)
                            lga.save()
                            
                            lga = LGA.objects.get(lga=new)
                            if lga.population != 0:
                                lga.population -= 1
                                print(lga.population)
                                lga.save()
                        
                        
                    if family_size !=None:
                        profile_update.family_size = family_size
                        
                    if dob !=None:
                        profile_update.dob = dob
                    
                    
                    profile_update.save()
                    messages.success(request, 'Profile has been updated!')
                    context = {
                        'form':form,
                        'form2':form2,
                    }
                    return render(request, 'admin/create_users.html', context)
                    
                else:
                    if not request.user.is_staff:
                        user = request.user
                    else:
                        messages.error(request, f'Form errors found!')
                        
                        context = {
                            'form':form,
                            'form2':form2,
                        }
                        return render(request, 'admin/create_users.html', context)
                        
                    profile = form.save(commit=False)
                    profile.user = user
                    
                    print('do not have any profile')
                    lga = LGA.objects.get(lga=lga)
                    lga.population += 1
                    lga.save()
                    
                    profile.save()
                    
                    messages.success(request, f'User has been Created!')
                    context = {
                        'form':form,
                        'form2':form2,
                    }
                
                    return render(request, 'admin/create_users.html', context)
        else:
            messages.error(request, f'Form errors found!')
            context = {
                'form':form,
                'form2':form2,
            }
            return render(request, 'admin/create_users.html', context)


class SettingsView(LoginRequiredMixin, View):
    login_url = '/login'          
        
    def get(self, request):
        user = Accounts.objects.get(id=request.user.id)
        context = {
            'user_details':user,           
        }
        return render(request, 'users/settings.html', context)
    
    def post(self, request):
        
        if 'email' in request.POST:
            email = request.POST.get('email')
            old_password = request.POST.get('oldP')
            email_exists = Accounts.objects.filter(email=email).exists()
            if not email_exists:
                user = authenticate(request, username=request.user, password=old_password)
                if user:
                    acct = Accounts.objects.get(id=request.user.id)
                    acct.email = email.lower()
                    acct.save()
                
                    messages.success(request, (f'{acct.username} your email has been changed'))
                    return redirect('users:settings')
                    
                else:
                    messages.error(request, 'Incorrect Current password!')
                    return redirect('users:settings')
            else:
                messages.error(request, 'Email Exists already!')
                return redirect('users:settings')
            
        if 'password1' in request.POST:
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            old_password = request.POST.get('old')
            
            if password1 != password:
                messages.error(request, 'Passwords Don\'t match!')
                return redirect('users:settings')
            else:
                user = authenticate(request, username=request.user, password=old_password)
                if user:
                    acct = Accounts.objects.get(id=request.user.id)
                    acct.set_password(password1)
                    acct.save()
                    messages.success(request, 'Password Changed try loggin in again!')
                    return redirect('auth:login')                    
                else:
                    messages.error(request, 'Incorrect Current password!')
                    return redirect('users:settings')
    

class UserInfoView(LoginRequiredMixin, View):
    
    def post(self, request):
        login_url = '/login'
        
        supplied = 2
        not_supplied = 0
        
        try:
            info = UserProfile.objects.get(user=request.user)
            if info.profile_pic:
                supplied += 1
            else:
                not_supplied += 1
            
            if info.lastName:
                supplied += 1
            else:
                not_supplied += 1
                
            if info.firstName:
                supplied += 1
            else:
                not_supplied += 1
            
            if info.otherName:
                supplied += 1
            else:
                not_supplied += 1
            
            if info.address:
                supplied += 1
            else:
                not_supplied += 1
                
            if info.phoneNumber:
                supplied += 1
            else:
                not_supplied += 1
                
            if info.gender:
                supplied += 1
            else:
                not_supplied += 1
                
            if info.religion:
                supplied += 1
            else:
                not_supplied += 1
                
            if info.family_size:
                supplied += 1
            else:
                not_supplied += 1
                
            finalRep = {
                'supplied':supplied,
                'not_supplied':not_supplied
            }
        except:
            finalRep = {
                'supplied':supplied,
                'not_supplied':not_supplied
            }
        return JsonResponse({'InfoDetails':finalRep}, safe=False)
    