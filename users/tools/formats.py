class upload_path:

    def get_extension(filename):
        extension = ''  # Initialize extension variable
        found = False  # Flag to indicate if a dot has been found
        
        # Extract the file extension from the filename
        for char in filename:
            if char == '.':
                found = True  # Set flag if dot is found
            if found:
                extension += char  # Append characters after the dot
        return extension.lower()  # Return the extension in lowercase

    def profile_picture(instance, filename):
        username = instance.user.username.lower()
        extension = upload_path.get_extension(filename) 
        path = f'users/{username}/images/' 
        file = f'profile_picture{extension}'

        return path + file 
    
class _format:

    def full_name(user, format):
        # Extract first, middle, and last names from the user object
        first = user.first_name
        middle = user.middle_name
        middle_initial = False
        
        # Check if middle name exists and get its initial
        if middle:
            middle_initial = user.middle_name[0]
        last = user.last_name
        
        # Format the name based on the specified format
        if format == 'standard':
            name = f'{first} {middle} {last}'  # Standard format
            formatted = name.title()  # Capitalize each word
        elif format == 'L, F':
            name = f'{last}, {first} {middle}'  # Last, First format
            formatted = name.title()  # Capitalize each word
        elif format == 'L, F MI':
            # Last, First with Middle Initial format
            if middle_initial:
                name = f'{last}, {first} {middle_initial}.'
            else:
                name = f'{last}, {first}'
            formatted = name.title()  # Capitalize each word
        elif format == 'path':
            # Path format for file storage
            name = f'{last}_{first}_{middle}'
            formatted = name.lower()  # Convert to lowercase

        return formatted  # Return the formatted name