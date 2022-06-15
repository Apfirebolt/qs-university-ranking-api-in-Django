from django.urls import path, include
from api.views import CreateCustomUserApiView, CustomTokenObtainPairView, ListUniversityApiView, CreateApiKeyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('register', CreateCustomUserApiView.as_view(), name='api-register'),
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('create-api-key', CreateApiKeyView.as_view(), name='api_key_create'),
    path('university', ListUniversityApiView.as_view(), name='university-list'),
]