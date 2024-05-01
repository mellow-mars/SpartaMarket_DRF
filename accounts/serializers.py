from .models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'nickname',
                  'birthday', 'gender', 'introduction')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields.pop('password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        validate_password(value)
        return value

class PasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password',)
    
    def validate(self, data):
        new_password = data.get('password')
        validate_password(new_password)
        user = self.instance

        if user and check_password(new_password, user.password):
            raise ValidationError("새로운 비밀번호는 이전 비밀번호와 달라야 합니다.")
        return data
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
