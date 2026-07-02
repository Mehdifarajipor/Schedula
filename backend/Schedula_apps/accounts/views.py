import logging

from django.contrib.auth import update_session_auth_hash

import rest_framework.permissions
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ( RegisterSerializer, UserProfileSerializer,
                          PasswordChangeSerializer )
from .models import User

# Create your views here.

logger = logging.getLogger(__name__)


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


class PasswordChangeAPIView(APIView):
    """
        POST /api/accounts/password-change/

        Body:
            old_password     : رمز فعلی
            new_password     : رمز جدید
            confirm_password : تکرار رمز جدید

        نیاز به احراز هویت دارد (IsAuthenticated).
        بعد از موفقیت، session کاربر حفظ می‌شود (logout نمی‌شود).
        """
    permission_classes = [rest_framework.permissions.IsAuthenticated]
    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        update_session_auth_hash(request, user)
        logger.info("Password changed for user pk=%s", user.pk)
        return Response({"your password was changed successfully!"}, status=status.HTTP_200_OK)

