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