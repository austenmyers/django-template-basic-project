class HelpText:
    user_account = {
        'username': 'Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        'is_active': 'Determines whether the user can login.',
        'is_staff': 'Determines whether the user can login to the admin site.',
        'date_joined': 'The date the user account was created.',     
        'email': 'Required. Must be a valid email address.', 
    }
    user_profile = {
        'first_name': 'Required. Legal first name.',
        'middle_name': 'Leave blank if no middle name.',
        'last_name': 'Required. Legal last name.',
        'display_name': 'Optional: Enter the name exactly as it should be displayed.',
        'profile_picture': 'Should clearly show the user\'s face.',       
    }