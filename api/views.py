from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from . serializers import CustomUserSerializer, ListCustomUserSerializer, CustomTokenObtainPairSerializer, \
    UniversitySerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from . models import CustomUser, University


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class ChangeSettingsApiView(UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]


class ListUniversityApiView(ListAPIView):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    permission_classes = [IsAuthenticated]




