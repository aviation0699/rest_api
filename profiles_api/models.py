from pickle import NONE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """"create a new user profile"""
        if not email:
            raise ValueError("must have have a email")
        email=self.normalize_email(email)
        user =self.model(email=email,name=name)
        user.set_password(password)#to keep password encrypted
        user.save(using=self.db)# to make the sure database is attached

        return user
    def create_superuser(self,email,name,password):
        """"create and save new super user with given details"""

        user=self.create_user(email,name,password)
        user.is_superuser=True  # created by permission mixin
        user.is_staff=(True)    # created by permission mixin
        user.save(using=self.db)
        return user



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