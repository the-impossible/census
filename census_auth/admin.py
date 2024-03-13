# My Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# My app imports
from census_auth.models import Accounts

# Register your models here.
class UserAccount(UserAdmin):
    list_display = ('email', 'username', 'acct_id', 'date_joined', 'last_login', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Accounts, UserAccount)