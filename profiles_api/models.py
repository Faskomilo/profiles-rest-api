from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for User Profiles
    """
    
    def create_user(self, email, name, lastname=None, password=None):
        """
        Create a new User Profile
        """
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, lastname=lastname)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password, lastname = None):
        """
        Create a new User Profile with super user permissions
        """
        
        user = self.create_user(email, name, lastname, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50, unique=True)
    lastname = models.CharField(max_length=50, null=True)
    deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Retrieve name and last name of the user
        """
        return "{} {}".format(self.name, self.lastname)

    def toString():
        """
        Return the user information as a string
        """
        return "UserProfile[email={}, name={}, lastname={}, deleted={}, moderator={}]".format(
            self.email, self.name, self.lastname, self.deleted, self.is_staff)

    def __str__(self):
        """
        Return the user information as a string
        """
        return "{} {}, {}".format(
            self.name, self.lastname, self.email)