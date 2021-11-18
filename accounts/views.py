from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import UserSerializer
# Create your views here.
User = get_user_model()


class UserCreateApiView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
