import rest_framework.permissions
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, UserProfileSerializer
from .models import User

# Create your views here.


class RegisterApiView(APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    def post(self, request):
        de_serializer = RegisterSerializer(data=request.data)
        de_serializer.is_valid(raise_exception=True)
        user = de_serializer.save()
        return Response(
            {
                'id': user.id,
                'email': user.email,
                'message': "account was created"
            },
            status=status.HTTP_201_CREATED,
        )


class UserProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [rest_framework.permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user