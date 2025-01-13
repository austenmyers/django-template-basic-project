from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import UserAccount, UserProfile
from .forms import UserAccountCreationForm, UserAccountChangeForm
from .tools import _format


class UserProfileInline(StackedInline):
    model = UserProfile
    can_delete = False

class UserAccountAdmin(UserAdmin):
    model = UserAccount
    form = UserAccountChangeForm
    add_form = UserAccountCreationForm

    fieldsets = [
        ('Login Details', {
            'fields': [
                'username',
                'email',
                'password'
            ]
        }),
        ('Account Type', {
            'fields': [
                'is_active',
                'is_superuser',
            ]
        }),
    ]
    add_fieldsets = [
        ('Login Details', {
            'fields': [
                'username',
                'email',
                'password1',
                'password2',
            ]
        }),
        ('Account Type', {
            'fields': [
                'is_active',
                'is_superuser',
            ]
        }),
    ]  
    readonly_fields = [
        # List of fields that should be read-only in the admin interface
    ]
    search_fields = [
        'username', 
    ]
    ordering = [
        'username' 
    ]
    list_display = [
        'username', 
        'email',
    ]
    list_filter = [
        'is_active',
    ]

    # Determine which inline forms to display based on user permissions
    def get_inlines(self, request, user):
        inlines = [UserProfileInline]

        return inlines
        
    # Return the display name if available, otherwise format the full name
    def full_or_display_name(self, user):
        if user.display_name:
            return user.display_name
        else:
            return _format.full_name(user, format='standard')

# Unregister the default Group model from the admin site
admin.site.unregister(Group)

admin.site.register(UserAccount, UserAccountAdmin)