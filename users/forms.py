from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms as f
from .models import UserAccount, UserProfile


# Form for creating a new user, extending the built-in UserCreationForm
class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ['username',]

# Form for updating an existing user, extending the built-in UserChangeForm
class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ['username',]

class UserAccountUpdateForm(f.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'username',
            'email',
        ]

class UserProfileUpdateForm(f.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture',
            'first_name',
            'middle_name',
            'last_name',
            'display_name',
        ]