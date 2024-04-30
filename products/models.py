from django.db import models
from accounts.models import User


class Product(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to='./products')
    author = models.ForeignKey(
        User,to_field='username', on_delete=models.CASCADE, related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
