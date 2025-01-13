from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):
    # Test case for user manager functionalities

    def test_create_user(self):
        # Retrieve the user model
        User = get_user_model()
        # Create a normal user with a username and password
        user = User.objects.create_user(username="normaluser", password="foo")
        # Assert that the username is set correctly
        self.assertEqual(user.username, "normaluser")
        # Assert that the user is active by default
        self.assertTrue(user.is_active)
        # Assert that the user is not a staff member
        self.assertFalse(user.is_staff)
        # Assert that the user is not a superuser
        self.assertFalse(user.is_superuser)
        
        try:
            # Check if username is None for AbstractUser or does not exist for AbstractBaseUser
            self.assertIsNone(user.username)
        except AttributeError:
            # Ignore if the user model does not have a username attribute
            pass
        
        # Test that creating a user without arguments raises a TypeError
        with self.assertRaises(TypeError):
            User.objects.create_user()
        
        # Test that creating a user with an empty username raises a TypeError
        with self.assertRaises(TypeError):
            User.objects.create_user(username="")
        
        # Test that creating a user with an empty username and a password raises a ValueError
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", password="foo")

    def test_create_superuser(self):
        # Retrieve the user model
        User = get_user_model()
        # Create a superuser with a username and password
        admin_user = User.objects.create_superuser(username="superuser", password="foo")
        # Assert that the username is set correctly for the superuser
        self.assertEqual(admin_user.username, "superuser")
        # Assert that the superuser is active
        self.assertTrue(admin_user.is_active)
        # Assert that the superuser is a staff member
        self.assertTrue(admin_user.is_staff)
        # Assert that the superuser is indeed a superuser
        self.assertTrue(admin_user.is_superuser)
        
        try:
            # Check if username is None for AbstractUser or does not exist for AbstractBaseUser
            self.assertIsNone(admin_user.username)
        except AttributeError:
            # Ignore if the user model does not have a username attribute
            pass

        # Test that creating a superuser with is_superuser set to False raises a ValueError
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="superuser", password="foo", is_superuser=False)