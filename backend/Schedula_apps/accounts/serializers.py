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


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if user.check_password(value):
            return value
        raise serializers.ValidationError({'old_password': 'your password is not valid!!!'})

    def validate_new_password(self, value):
        user = self.context['request'].user
        password_validation.validate_password(value, user)
        return value

    def validate(self, data):
        if data['confirm_password'] != data['new_password']:
            raise serializers.ValidationError({'confirm_password': 'the passwords do not match!!!'})
        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError({'new_password': 'your password can not be same like your old password'})
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save(update_fields=['password'])
        return user