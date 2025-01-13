from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


# Custom manager for user creation, extending the default BaseUserManager
class UserAccountManager(BaseUserManager):

    # Create and return a regular user with the given username and password
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    # Create and return a superuser with the given username and password
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Validate that the superuser has staff privileges
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser requires is_staff=True'))
        
        # Validate that the superuser has superuser privileges
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser requires is_superuser=True'))
        
        return self.create_user(username, password, **extra_fields)