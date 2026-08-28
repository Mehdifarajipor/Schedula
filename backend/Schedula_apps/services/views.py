from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Service
from .serializers import ServiceSerializer
from .permissions import IsProvider

# Create your views here.


class ServiceAPIViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action in [
            "create", "update", "partial_update", "destroy",
        ]:
            return [IsProvider()]
        return [AllowAny()]

