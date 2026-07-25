from django.contrib import admin

from .models import User, ProviderProfile

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'phone_number', 'role', 'date_joined']


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'business_name', 'email']
    prepopulated_fields = {'slug': ['business_name']}
