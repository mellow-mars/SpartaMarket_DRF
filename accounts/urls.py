from django.urls import path
from .views import (
    UserAPIView, 
    PasswordChangeAPIView, 
    UserDeleteAPIView,
    LogoutAPIView
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("password/", PasswordChangeAPIView.as_view()),
    path("delete/", UserDeleteAPIView.as_view()),
    path("<str:username>/", UserAPIView.as_view()),
]
