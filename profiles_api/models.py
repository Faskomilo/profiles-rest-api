from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """
    Manager for User Profiles
    """
    
    def create_user(self, email, first_name, last_name=None, password=None):
        """
        Create a new User Profile
        """
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Create a new User Profile with super user permissions
        """
        
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, null=True)
    deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """
        Retrieve first_name and last first_name of the user
        """
        return "{} {}".format(self.first_name, self.last_name)

    def toString(self):
        """
        Return the user information as a string
        """
        return "UserProfile[email={}, first_name={}, last_name={}, deleted={}, moderator={}]".format(
            self.email, self.first_name, self.last_name, self.deleted, self.is_staff)

    def __str__(self):
        """
        Return the user information as a string
        """
        return "{} {}, {}".format(
            self.first_name, self.last_name, self.email)

class ProfileFeedItems(models.Model):
    """
    Profile status
    """

    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text

