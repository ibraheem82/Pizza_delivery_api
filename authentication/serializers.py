from .models import User
from rest_framework import serializers
from phonenumber_field.modelfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, unique=True)
    email = serializers.EmailField(max_length=90, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)
