from django.db import models


from ..accounts.models import ProviderProfile

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name


class Service(models.Model):
    provider = models.ForeignKey(ProviderProfile, models.CASCADE, "services")
    category = models.ForeignKey(Category, models.SET_NULL, "services", null=True)

    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="minutes")

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class ServiceImage(models.Model):
    service = models.ForeignKey(Service, models.CASCADE, "images")
    file = models.ImageField(upload_to="services/")
