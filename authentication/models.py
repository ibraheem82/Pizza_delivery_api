from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
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

# This is a method definition for creating a superuser with specified fields.
    def create_superuser(self, email, password, **extra_fields):

      # These lines set default values for is_staff, is_superuser, and is_active in extra_fields to True.
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


# These lines check that is_staff, is_superuser, and is_active in extra_fields are all True, and raise a ValueError with a corresponding message if any of them are not.
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is staff as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is superuser as True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is active as True"))

          # This line calls the create_user method in the CustomUserManager class with the provided email, password, and extra_fields.
        return self.create_user(email, password, **extra_fields)


# * This is a model class called User that inherits from the AbstractUser model.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=90, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)


# * These class variables specify that the email field should be used as the unique identifier for a User, and that username and phone_number are required fields when creating a User.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']


# This line assigns an instance of the CustomUserManager class to the objects attribute of the User class, which allows us to use the create_user and create_superuser methods defined in CustomUserManager to create User objects.
    objects = CustomUserManager()


# This is a special method that returns a string representation of a User object, which in this case is simply the user's email address.

    def __str__(self):
        return f"<User {self.email}"
