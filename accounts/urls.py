from django.contrib import admin
from django.urls import path
from .views import UserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", TokenRefreshView.as_view()),
    path("<str:username>/", UserAPIView.as_view()),
]
