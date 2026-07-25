import logging

from django.contrib.auth import update_session_auth_hash

import rest_framework.permissions
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from .serializers import ( RegisterSerializer, UserProfileSerializer,PasswordChangeSerializer,
                           PasswordResetRequestSerializer,PasswordResetConfirmSerializer,
                           ProviderProfileSerializer,)
from .models import User, ProviderProfile
from .emails import send_reset_email

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


class PasswordResetRequestView(APIView):
    """
        POST /api/accounts/password-reset/

        Body:
            email : آدرس ایمیل کاربر

        نکته امنیتی: در هر صورت (ایمیل وجود داشته باشد یا نه)
        پیام یکسانی برمی‌گردد تا از user enumeration جلوگیری شود.
        """
    permission_classes = [rest_framework.permissions.AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        if user is not None:
            try:
                send_reset_email(user, request)
                logger.info("Password reset request for user pk=%s sent", user.pk)
            except Exception as e:
                logger.exception("Failed to send password reset email for user pk=%s", user.pk)
                raise

            return Response({"detail: sent an email for reset password"}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(APIView):
    """
       POST /api/accounts/password-reset/<uid>/<token>/

       Body:
           uid              : از URL
           token            : از URL
           new_password     : رمز جدید
           confirm_password : تکرار رمز جدید

       Token یک‌بار مصرف است و بعد از استفاده یا تغییر رمز باطل می‌شود.
       """
    permission_classes = [rest_framework.permissions.AllowAny]

    def post(self, request, uid, token):
        data = {**request.data, "uid": uid, "token": token}
        serializer = PasswordResetConfirmSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer._user
        logger.info("Password reset completed for user pk=%s", user.pk)
        return Response(
            {"detail": "Password reset completed successfully! user can login with new password now"},
            status=status.HTTP_200_OK
        )


@api_view(['GET', 'PATCH'])
def provider_profile(request: Request):
    p_profile = ProviderProfile.objects.get(user=request.user)
    if request.method == "GET":
        serializer = ProviderProfileSerializer(instance=p_profile)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializer = ProviderProfileSerializer(instance=p_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
           return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

