from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


app_name = "accounts"


urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path("me/",views.UserProfileAPIView.as_view(),name="user_profile"),
    path("password_change/", views.PasswordChangeAPIView.as_view(), name="password_change"),
    path("password_reset/", views.PasswordResetRequestView.as_view(), name="password_reset_request"),
    path("password_reset/<str:uid>/<str:token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("provider-profile/", views.provider_profile, name='provider_profile'),
]