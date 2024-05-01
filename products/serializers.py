from .models import Product
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title','content','image')
