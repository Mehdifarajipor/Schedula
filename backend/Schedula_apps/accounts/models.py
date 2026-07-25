from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

# Create your models here.


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        PROVIDER = "PROVIDER", "Provider"
        ADMIN = "ADMIN", "Admin"

    # fields
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    avatar = models.ImageField(upload_to="users/avatars/", null=True, blank=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=RoleChoices.choices, default=RoleChoices.CUSTOMER)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # settings
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    # managers
    objects = UserManager()

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return f"{self.username if self.username else ''}: {self.email}"


class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="provider_profile")

    # --- Business Identity ---
    business_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    bio = models.TextField(blank=True)

    # --- Contact ---
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField()

    # --- Location ---
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # --- Business Settings ---
    timezone = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)

    # --- Booking Settings ---
    appointment_buffer = models.PositiveIntegerField(default=0)
    # the distance between the turns(minutes)
    advance_booking_days = models.PositiveIntegerField(default=30)
    # to make an appointment a few days ahead(days)
    cancellation_policy = models.TextField(blank=True)

    # --- Rating / Trust ---
    rating = models.FloatField(default=0)
    total_reviews = models.PositiveIntegerField(default=0)

    # --- Media ---
    logo = models.ImageField(upload_to="providers/logos/", null=True, blank=True)

    # --- System ---
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name






