# My django imports
from django.urls import path

# My app imports
from census_auth.views import (
    LoginView,
    RegisterView,
    EmailValidationView,
    UsernameValidationView,
    DashboardView,
    LogoutView,
)
app_name = 'auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('validate-email', EmailValidationView.as_view(), name='validate-email'),
    path('validate-username', UsernameValidationView.as_view(), name='validate-username'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]