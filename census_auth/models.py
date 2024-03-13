from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, nin, email, password=None):

        if not email:
            raise ValueError('Email address required!')
        if len(nin) > 10 or len(nin) < 10:
            raise ValueError('Length of NIN should not be greater or less than 10')
        if not nin:
            raise ValueError('NIN required!')
        if password is None:
            raise ValueError('Password is required')

        user = self.model(email=self.normalize_email(email), username=nin)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        # create a superuser with the given email, firstname and password
        if password is None:
            raise TypeError('Password should not be empty')

        user = self.create_user(email=self.normalize_email(email), password=password, username=username.lower())

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Accounts(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True, null=True)
    username = models.CharField(max_length=10, unique=True)
    acct_id = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'Accounts'
        verbose_name_plural = 'Accounts'