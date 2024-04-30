from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'nickname',
                  'birthday', 'gender', 'introduction')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
