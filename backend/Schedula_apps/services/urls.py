from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'services'

router = DefaultRouter()
router.register("", views.ServiceAPIViewSet, basename="services")

urlpatterns = [
    path("", include(router.urls)),
]