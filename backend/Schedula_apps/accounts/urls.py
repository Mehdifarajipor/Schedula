from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views


app_name = "accounts"


urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]