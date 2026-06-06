from django.contrib.auth import password_validation

from rest_framework import serializers

from .services import UserServices
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=11, min_length=11)
    username = serializers.CharField(max_length=250)
    password = serializers.CharField(write_only=True, min_length=8, max_length=250)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'username', 'password']

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        return UserServices.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'avatar','phone_number', 'first_name', 'last_name', 'date_joined']
        read_only_fields = (
            'id',
            'email'
        )