from django.db import models

# Create your models here.
#custom models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    def has_module_perms(self, app_label):
        return self.is_superuser
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True)
    password=models.CharField( max_length=100,null=True,blank=True)
    forget_password = models.CharField( max_length=100,null=True,blank=True)
    email_token=models.CharField(max_length=100,null=True,blank=True)

    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email
