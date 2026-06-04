from .models import User
from django.shortcuts import get_object_or_404


class UserServices:
    @staticmethod
    def create_user(**validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

    @staticmethod
    def update_user(user, **validated_data):
        for key, value in validated_data.items():
            setattr(user, key, value)
        user.save()
        return user


