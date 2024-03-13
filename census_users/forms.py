from django import forms
# My app imports
from census_users.models import UserProfile
from census_admin.models import LGA


class UserProfileForm(forms.ModelForm):
    
    gender_options = [
        (1, 'Male'),
        (2, 'Female'),
    ]
    
    religion_options = [
        (0, '--- Select an option ---'),
        (1, 'Christianity'),
        (2, 'Muslim'),
    ]
    
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput(
                                   attrs={
                                       'class':'form-control',
                                       'type':'file',
                                        'accept':'image/png, image/jpeg'                                
                                   }
                               ))
    
    gender = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(
                                            attrs={
                                                'class':'form-check-input',
                                                'type':'checkbox',
                                            }),
                                            choices=gender_options,
                                        )
    
    religion = forms.ChoiceField(required=False, choices=religion_options,
                                widget=forms.Select(
                                    attrs={
                                        'class':'custom-select'
                                    }
                                ))
    
    lga = forms.ModelChoiceField(queryset=LGA.objects.all(), initial=1, required=True,
                            widget=forms.Select(
                                attrs={
                                    'class':'custom-select'
                                }
                            ))
    
    lastName = forms.CharField(max_length=30, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Last Name',
                                            'required':'false'
                                        }
                            ))
    
    family_size = forms.CharField(max_length=3, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Family Size',
                                            'type':'number',
                                        }
                            ))
    
    firstName = forms.CharField(max_length=30, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'First Name',
                                        }
                            ))
    
    otherName = forms.CharField(required=False, max_length=30, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Other Name',
                                        }
                            ))
    
    phoneNumber = forms.CharField(max_length=255, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Phone Number',
                                            'type':'number',
                                        }
                            ))
    
    dob = forms.CharField(max_length=20, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Date of Birth',
                                            'type':'date',
                                        }
                            ))
    
    
    address = forms.CharField(max_length=255, widget=forms.TextInput(
                                        attrs={
                                            'class':'form-control',
                                            'placeholder':'Address',
                                        }
                                ))
    
     
    class Meta():
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'date_created']
    
    # def clean_profile_pic(self):
    #     supposed_profile_pic = str(self.cleaned_data.get('profile_pic')).split('.')
    #     profile_pic = str(self.cleaned_data.get('profile_pic'))
        
    #     if len(supposed_profile_pic) > 2:
    #         raise forms.ValidationError('Rename file properly, separate(_) words with underscores rather than periods(.)')
    #     return profile_pic
        