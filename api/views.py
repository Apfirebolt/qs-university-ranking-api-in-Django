from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from . pagination import StandardResultsSetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
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
    permission_classes = [HasAPIKey | IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    throttle_classes = [UserRateThrottle]
    queryset = University.objects.all()
    search_fields = (
        '^name',
        '^country'
    )
    ordering_fields = (
        'country',
        'name',
        'rank',
        'ar_score',
        'ar_rank'
    )


class CreateApiKeyView(APIView):

    def post(self, request):
        """Generate API Key."""
        username = request.data.get('name')
        if username:
            api_key, key = APIKey.objects.create_key(name=username)
            return Response({'name':str(api_key), 'key': str(key)}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
    



