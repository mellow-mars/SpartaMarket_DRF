from .models import Product
from rest_framework import serializers
from rest_framework.authtoken.models import Token

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"
#         read_only_fields = ("article",)

#     def to_representation(self, instance):
#         ret = super().to_representation(instance)
#         ret.pop('article')
#         return ret


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title','content','image')
