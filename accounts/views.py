from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import PasswordChangeSerializer, UserSerializer


class UserAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, username):

        user = request.user
        if user.username == username:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, username):

        user = request.user
        if user.username == username:
            serializer = UserSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class PasswordChangeAPIView(APIView):

    def put(self, request):
        user = get_object_or_404(User, username=request.user.username)
        if request.user.username == user.username:
            serializer = PasswordChangeSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserDeleteAPIView(APIView):

    def delete(self, request):
        user = request.user
        password = request.data.get('password')
        if user.check_password(password):
            user.delete()
            return Response({"message": "회원탈퇴가 완료되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "리프레시 토큰이 제공되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)
