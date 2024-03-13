# My django imports
from django.urls import path

# My app imports
from census_users.views import (
    HomeView,
    ContactView,
    AboutView,
    UserProfileView,
    SettingsView,
    UserInfoView,
)
app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    
    path('user_info/', UserInfoView.as_view(), name='user_info'),
    path('user_profile_create', UserProfileView.as_view(), name='admin_create_users'),
     
    path('settings', SettingsView.as_view(), name='settings'),
    
      
]