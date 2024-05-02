from pickle import NONE
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class ProductListAPIView(APIView):

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    def get_object(self, product_id):
        return get_object_or_404(Product, id=product_id)

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 6

        post = Product.objects.all()
        page = paginator.paginate_queryset(post, request)
        serializer = ProductSerializer(page, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, product_id):
        post = self.get_object(product_id)
        if request.user == post.author:
            serializer = ProductSerializer(
                post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, product_id):
        post = self.get_object(product_id)
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
