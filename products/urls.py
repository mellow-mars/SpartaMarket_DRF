from django.urls import path
from .views import ProductListAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view()),
    path("<int:product_id>", ProductListAPIView.as_view()),
]
