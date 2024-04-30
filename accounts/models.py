from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ("F", "여성"),
        ("M", "남성"),
        ("O", "기타")
    )
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    introduction = models.TextField(blank=True)
    birthday = models.DateField()
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')
    email = models.EmailField(max_length=254, unique=True)
