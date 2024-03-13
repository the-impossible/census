# My django imports
from random import randint
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages #for sending messages
from django.views import View

# My app imports
from census_auth.models import Accounts
from census_admin.models import LGA
from census_users.models import UserProfile, ContactSupport
from census_users.forms import UserProfileForm
from census_auth.forms import RegistrationForm

# Create your views here.
class AdminDashboardView(LoginRequiredMixin, View):
    
    def get(self, request):             
        first_six_users = Accounts.objects.filter(is_staff=False).order_by('-id')[:4]
        first_six_staffs = Accounts.objects.filter(is_staff=True, is_superuser=False).order_by('-id')[:4]
        population = Accounts.objects.filter(is_staff=False).count()
        reg_centers = Accounts.objects.filter(is_staff=True, is_superuser=False).count()
        lga = LGA.objects.all().count()
        context = {
            'user':request.user,
            'first_six_users':first_six_users,
            'first_six_staffs':first_six_staffs,
            'population':population,
            'reg_centers':reg_centers,
            'lga':lga,
        }
        
        try:
            profile = UserProfile.objects.get(user_id=request.user.id)
            context = {
                'profile':profile,
                'user':request.user,
                'first_six_users':first_six_users,
                'first_six_staffs':first_six_staffs,
                'population':population,
                'reg_centers':reg_centers,
                'lga':lga,
            }
        except:
            pass
    
        return render(request, 'admin/dashboard.html', context)
    
    def post(self, request):
        first_six_users = Accounts.objects.filter(is_staff=False).order_by('-id')[:4]
        first_six_staffs = Accounts.objects.filter(is_staff=True, is_superuser=False).order_by('-id')[:4]
        population = Accounts.objects.filter(is_staff=False).count()
        reg_centers = Accounts.objects.filter(is_staff=True, is_superuser=False).count()
        lga = LGA.objects.all().count()
        posted = request.POST
        if 'lga' in posted:
            try:
                LGA.objects.get(lga=posted['lga'].lower())
                messages.warning(request, f"LGA: has been created before")
            except:
                LGA.objects.create(lga=posted['lga'].lower())
                messages.success(request, f"category: {posted['lga']} has been created successfully")
                
        context = {
            'user':request.user,
            'first_six_users':first_six_users,
            'first_six_staffs':first_six_staffs,
            'population':population,
            'reg_centers':reg_centers,
            'lga':lga,
        }
        return render(request, 'admin/dashboard.html', context)
    
class AdminUserListView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        try:        
            only_users = Accounts.objects.filter(is_staff=False).order_by('-id')
            context = {
                'only_users':only_users,    
            }            
            return render(request, 'admin/list_users.html', context)
        except:
            return render(request, 'admin/list_users.html')

class AdminUserDetailView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            context = {
                'user_details':user,
            }
        
            return render(request, 'admin/user_details.html', context)
        except:
            
            return render(request, 'admin/user_details.html')

class AdminUserEditView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            profile = UserProfile.objects.get(user_id=user_id)
            form1 = UserProfileForm(instance=profile)
            context = {
                'user_details':user,
                'form1':form1,
            }
            return render(request, 'admin/admin_user_edit.html', context)
        except:
            return render(request, 'admin/admin_user_edit.html')
        
    def post(self, request, user_id):
        
        user = Accounts.objects.get(id=user_id)
        form1 = UserProfileForm(request.POST, request.FILES, instance=user)
                    
        if form1.is_valid():
            # print(form1)
            profile_pic = form1.cleaned_data.get('profile_pic')
            lastName = form1.cleaned_data.get('lastName')
            firstName = form1.cleaned_data.get('firstName')
            otherName = form1.cleaned_data.get('otherName')
            address = form1.cleaned_data.get('address')
            phoneNumber = form1.cleaned_data.get('phoneNumber')
            gender = form1.cleaned_data.get('gender')
            religion = form1.cleaned_data.get('religion')
            lga = form1.cleaned_data.get('lga')
            family_size = form1.cleaned_data.get('family_size')
            dob = form1.cleaned_data.get('dob')
            
            profile_update = UserProfile.objects.get(user_id=user.id)
            
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
                
            if family_size !=None:
                profile_update.family_size = family_size
                
            if dob !=None:
                profile_update.dob = dob
                
            if lga !=None:
                new = profile_update.lga
                profile_update.lga = lga
                
                if profile_update.lga != lga:
                    print('updating...')
                    
                    lga = LGA.objects.get(lga=lga)
                    lga.population += 1
                    lga.save()
                    
                    lga = LGA.objects.get(lga=new)
                    if lga.population != 0:
                        lga.population -= 1
                        print(lga.population)
                        lga.save()
                
                
            profile_update.save()
            messages.success(request, f'{user.username} has been Edited!')
            
            return redirect('staff:admin_user_details', user_id)
        else:
            # messages.error(request, f'User not found!')
            context = {
                'user':user,
                'form1':form1,
            }
            return render(request, 'admin/admin_user_edit.html', context)
        
class AdminUserDeleteView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            context = {
                'user_details':user,
            }
        
            return render(request, 'admin/delete_user.html', context)
        except:
            return render(request, 'admin/delete_user.html')
        
    def post(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            username = user.username
            user.delete()
            messages.success(request, f'{username} has been deleted!')
            return redirect('staff:admin_user_list')
        except:
            messages.error(request, f'User not found!')
            return redirect('staff:admin_user_list')
        
class AdminCreateStaffView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        
        form = RegistrationForm()
        context = {
            'form':form,
        }
        return render(request, 'admin/create_staffs.html', context)
    
    def post(self, request):
        
        def generate_id():
            id = 'CBCIM0' + str(randint(80, 1000))
            found = Accounts.objects.filter(acct_id=id)
            if found:
                generate_id()
                
            return id
        
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.set_password(user.password)        
            user.acct_id = generate_id()
            user.is_staff = True
            user.save()
            messages.success(request, 'Staff Account has been created!')
            
            context = {
                'form':RegistrationForm(),
            }
            return render(request, 'admin/create_staffs.html', context)

        else:
            messages.error(request, f'Form errors found!')
            context = {
                'form':form,
            }
            return render(request, 'admin/create_staffs.html', context)
        
class AdminLGAListView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        try:        
            lga = LGA.objects.all().order_by('-id')
            context = {
                'lga':lga,
            }            
            return render(request, 'admin/list_lga.html', context)
        except:
            return render(request, 'admin/list_lga.html')

class AdminLGADeleteView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        try:
            lga = LGA.objects.get(id=user_id)
            context = {
                'lga':lga,
            }
            return render(request, 'admin/delete_lga.html', context)
        except:
            return render(request, 'admin/delete_lga.html')
        
    def post(self, request, user_id):
        try:
            user = LGA.objects.get(id=user_id)
            lga = user.lga
            user.delete()
            messages.success(request, f'{lga} has been deleted!')
            return redirect('staff:admin_lga_list')
        except:
            messages.error(request, f'LGA not found!')
            return redirect('staff:admin_lga_list')
    
class AdminStaffListView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        try:        
            only_staffs = Accounts.objects.filter(is_staff=True, is_superuser=False).order_by('-id')
            context = {
                'only_staffs':only_staffs,
            }
        except:
            context = {}
        return render(request, 'admin/list_staff.html', context)
    
class AdminStaffDetailView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            context = {
                'user':user,
            }
        
            return render(request, 'admin/staff_details.html', context)
        except:
            return render(request, 'admin/staff_details.html')

class AdminStaffDeleteView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            context = {
                'user_details':user,
            }
        
            return render(request, 'admin/delete_staff.html', context)
        except:
            return render(request, 'admin/delete_staff.html')
        
    def post(self, request, user_id):
        try:
            user = Accounts.objects.get(id=user_id)
            username = user.username
            user.delete()
            messages.success(request, f'{username} has been deleted!')
            return redirect('staff:admin_staff_list')
        except:
            messages.error(request, f'User not found!')
            return redirect('staff:admin_staff_list')
        
class AdminStaffEditView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request, user_id):
        
        try:
            profile = UserProfile.objects.get(user_id=user_id)
            form = UserProfileForm(instance=profile)
        except:
            form = UserProfileForm()
        
        context = {
            'form':form,
        }
        
        return render(request, 'admin/edit_staff.html', context)
    
    def post(self, request, user_id):
        
        form = UserProfileForm(request.POST, request.FILES)
        
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
            
            entry = UserProfile.objects.filter(user_id=user_id).exists()

            if entry:
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
                    profile_update.lga = lga
                    
                if family_size !=None:
                    profile_update.family_size = family_size
                    
                if dob !=None:
                    profile_update.dob = dob
                    
                profile_update.save()
                messages.success(request, 'Profile has been updated!')
                context = {
                    'form':form,
                }
                return render(request, 'admin/edit_staff.html', context)
                
            else:
                user = request.user
                
                profile = form.save(commit=False)
                profile.user = user
                
                profile.save()
                messages.success(request, f'User has been created!')
                context = {
                    'form':UserProfileForm(),
                }
                return render(request, 'admin/edit_staff.html', context)
        else:
            messages.error(request, f'Form errors found!')
            context = {
                'form':form,
            }
            return render(request, 'admin/edit_staff.html', context)

class AdminSupportMessageView(LoginRequiredMixin, View):
    login_url = '/login'
    
    def get(self, request):
        message = ContactSupport.objects.all().order_by('-id')
        context = {
            'message':message,
        }           
        return render(request, 'admin/support_messages.html', context)
    
    def post(self, request):
        message_id = request.POST.get('message_id')
        message = ContactSupport.objects.get(id=message_id)
        if message.done:
            message.done = False
        else:
            message.done = True
        message.save()
        messages.success(request, 'The message status has changed')
        return redirect('staff:admin_support_message')
    
    