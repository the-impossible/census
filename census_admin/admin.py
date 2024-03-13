# My Django imports
from django.contrib import admin

# My app imports
from census_admin.models import (
    LGA,
)

# Register your models here.
admin.site.register(LGA)