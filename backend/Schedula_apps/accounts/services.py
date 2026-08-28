from .models import User, ProviderProfile

from django.shortcuts import get_object_or_404
from django.db import transaction


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


class ProviderProfileServices:
    @staticmethod
    @transaction.atomic
    def create_provider_profile(user, **validated_data):
        if user.is_authenticated:
            profile = ProviderProfile.objects.create(user=user, **validated_data)
            profile.save()
            profile.user.role = "PROVIDER"
            profile.user.save(update_fields=["role"])
            return profile
        return None

    @staticmethod
    def update_provider_profile(profile, **validated_data):
        for key, value in validated_data.items():
            setattr(profile, key, value)
        profile.save()
        return profile

