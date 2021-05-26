from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"Databse model for user in the system """
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)#check whether user field is activated
    is_staff=models.BooleanField(default=True)

    objects= UserProfileManager()

    USERNAME_FIELD="email" #to overrite the default  feild
    REQUIRED_FIELDS=["name"]

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    def get_short_name(self):
        """retrive short name of user"""
        return self.name
    def __str__(self):
        """return string representation of user""" 
        return self.email   