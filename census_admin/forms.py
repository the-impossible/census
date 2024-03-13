# My django imports
from django import forms
# from bot.validator import validate_file_size, validate_pic_size
from django.core.validators import FileExtensionValidator

# My app imports
from census_auth.models import Accounts


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=150,
                             widget=forms.TextInput(
                                attrs={
                                    'class':'form-control mb-2',
                                    'placeholder':'Username',
                                    'type':'text',
                                }
                             ))
    email = forms.EmailField(required=True, max_length=255, help_text='A valid email address is Required!',
                             widget=forms.TextInput(
                                attrs={
                                    'class':'form-control mb-2',
                                    'placeholder':'Email Address',
                                    'type':'email',
                                }
                             ))
    password = forms.CharField(required=True, help_text='Password must contain at least 6 characters',
                            widget=forms.TextInput(
                                attrs={
                                    'class':'form-control mb-2',
                                    'placeholder':'Password',
                                    'type':'password',
                                }
                            ))
    
    class Meta:
        model = Accounts
        fields = ('username', 'email', 'password')
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 6:
            raise forms.ValidationError('Password too short')
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()        
        if Accounts.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    