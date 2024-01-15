from django.conf import settings
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .models import Account
from .serializers import (AccountSerializer, CustomTokenObtainPairSerializer,
                          JWTCookieTokenRefreshSerializer)

# Create your views here.


class AccountViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):
        current_user_id = request.user.id
        user_id = request.query_params.get("user_id")

        if user_id:
            self.queryset = self.queryset.filter(id=user_id)
        else:
            self.queryset = self.queryset.filter(id=current_user_id)
        serializer = AccountSerializer(self.queryset, many=True)
        return Response(serializer.data)


class JWTSetCookieMixin:
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"],
                response.data["refresh"],
                max_age=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                httponly=True,
                samesite=settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"],
            )
        if response.data.get("access"):
            response.set_cookie(
                settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"],
                response.data["access"],
                max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                httponly=True,
                samesite=settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"],
            )
            
        del response.data["access"]

        return super().finalize_response(request, response, *args, **kwargs)


class JWTCookieTokenObtainPairView(JWTSetCookieMixin, TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class JWTCookieTokenRefreshView(JWTSetCookieMixin, TokenRefreshView):
    serializer_class = JWTCookieTokenRefreshSerializer