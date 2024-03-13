#My Django import
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now

# My app imports
from census_auth.models import Accounts
from census_admin.models import LGA
# from census_users.validator import validate_pic_size

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(Accounts, blank=True, null=True, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(default='auth/app-assets/img/profile.png', null=True, upload_to='auth/app-assets/img/profile_pics/', validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg',))])
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    otherName = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=30)
    gender = models.CharField(max_length=15, blank=True)
    religion = models.CharField(max_length=20)
    lga = models.ForeignKey(to=LGA, on_delete=models.CASCADE, related_name='user_lga')
    family_size = models.CharField(max_length=3)
    dob = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} opted in'
    
    @property
    def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url
    
    class Meta:
        db_table = 'User Profile'
        verbose_name_plural = 'User Profile'
        
class ContactSupport(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(default=now)
    message = models.TextField()
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.email} has Messaged CBCIMS'

    class Meta:
        db_table = 'Support Messages'
        verbose_name_plural = 'Support Messages'