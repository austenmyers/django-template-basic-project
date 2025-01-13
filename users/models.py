from django.db import models as dj
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserAccountManager
from .tools import HelpText, ErrorMessages, upload_path


class UserProfile(dj.Model):
    class Meta:
        verbose_name = 'User Profile'

    user = dj.OneToOneField(
        'users.UserAccount',
        on_delete=dj.CASCADE,
        related_name='user_profile',
    )
    
    # Names
    first_name = dj.CharField(
        max_length=250,
        verbose_name='First Name', 
        help_text=HelpText.user_profile['first_name'] 
    )
    middle_name = dj.CharField(
        blank=True,
        max_length=250, 
        verbose_name='Middle Name', 
        help_text=HelpText.user_profile['middle_name']
    )
    last_name = dj.CharField(
        max_length=250, 
        verbose_name='Last Name',
        help_text=HelpText.user_profile['last_name'] 
    )
    display_name = dj.CharField(
        max_length=250,
        blank=True, 
        verbose_name='Display Name',
        help_text=HelpText.user_profile['display_name']
    )
    
    # Profile Picture
    profile_picture = dj.ImageField(
        blank=True,
        upload_to=upload_path.profile_picture,
        verbose_name='Profile Picture',
        help_text=HelpText.user_profile['profile_picture']
    )


    def __str__(self):
        return self.user.username  
    
class UserAccount(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'User' 

    username_validator = UnicodeUsernameValidator()
    # The field used for authentication
    USERNAME_FIELD = 'username'  
    # Additional fields required when creating a superuser
    REQUIRED_FIELDS = []  
    # Custom manager for user creation and management
    objects = UserAccountManager()

    # Login Details
    username = dj.CharField(
        max_length=50,
        unique=True,
        help_text=_(HelpText.user_account['username']),
        validators=[username_validator],
        error_messages={
            'unique': _(ErrorMessages.user_account['username_unique']),
        },
    )
    email = dj.EmailField(
        verbose_name='e-mail',
        help_text=HelpText.user_account['email']
    )

    # Account Type
    is_active = dj.BooleanField(
        default=True, 
        verbose_name='Active User',
        help_text=HelpText.user_account['is_active'] 
    )
    is_staff = dj.BooleanField(
        default=False, 
        verbose_name='Staff Status',
        help_text=HelpText.user_account['is_staff'] 
    )
    date_joined = dj.DateTimeField(
        default=timezone.now,
        verbose_name='Date Joined',
        help_text=HelpText.user_account['date_joined']  
    )

    def get_user_profile(self):
        profile = UserProfile.objects.get(user=self)

        return profile
    
