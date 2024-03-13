# My Django imports
from django.contrib import admin

# My app imports
from census_users.models import (
    UserProfile,
    ContactSupport,
)

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ContactSupport)
