from django.contrib import admin

from .models import Category, Service, ServiceImage

# Register your models here.

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'provider', 'category']