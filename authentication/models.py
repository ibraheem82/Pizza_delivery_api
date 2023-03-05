from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.


# ** Defining a custom user model manager
# *  Custom user model managers are classes that provide a set of built-in methods which allow the developers to manage users and their data in the Django application. It helps developers to easily create, retrieve, update, and delete user objects from the database without writing custom code for every action. It also allows them to customize authentication/authorization process such as password checks or adding personal user permissions.
class CustomUserManager(BaseUserManager):
    # *  This code defines a custom user model manager, which is used to create and manage user accounts in the Django framework. The CustomUserManager class inherits from the BaseUserManager class, which provides default methods for creating and managing user accounts.

    # * The create_user() method is used to create new user accounts. It takes in an email address, password and any extra fields as arguments. The method first checks if the email address is provided, and raises a ValueError with the error message "Email should be provided" if it is not .

    # * The email address is then normalized to lower case using the normalize_email() method provided by Django. The new_user variable is created using the self.model attribute, which is the user model defined in the Django app. The email address and any extra fields are passed to the model as arguments.

    # * Finally, the set_password() method is used to set the user's password, using Django's built-in password hashing mechanism. This ensures that the user's password is securely stored in the database.

 # * Defining a method to create new users
    def create_user(self, email, password, **extra_fields):

      # ! Check if email is provided, if not raise an error
        if not email:
            raise ValueError(_("Email should be provided"))
          # *  Normalize email to lower case
        email = self.normalize_email(email)
        # * Create a new user with email and extra fields
        new_user = self.model(email=email, **extra_fields)

        # * Set user password using Django's built-in password hashing mechanism
        new_user.set_password(password)


# *  new_user.save() is a method used to save the user's data in a database. It takes the details of the new user, such as name and email address, and stores them in the database so they can be retrieved later if needed. This method will return an object containing the newly created user's information once it has been successfully saved.
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
