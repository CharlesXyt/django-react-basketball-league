from django.conf import settings
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .models import Account, Role
from .serializers import (AccountSerializer, CustomTokenObtainPairSerializer,
                          JWTCookieTokenRefreshSerializer)

# Create your views here.

class AccountViewSet(APIView):
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        user_id = request.query_params.get("user_id")        

        if user_id and user_id != current_user.id:
            if current_user.role.name == Role.player:
                raise PermissionDenied('Player cannot access other user information')
            elif current_user.role.name == Role.coach:
                self.queryset = self.queryset.filter(team=current_user.team).get(id=user_id)
                if not self.queryset:
                    raise PermissionDenied('You cannot access this user information')
            else:
                self.queryset = self.queryset.get(id=user_id)
        else:
            self.queryset = self.queryset.get(id=current_user.id)
        
        serializer = AccountSerializer(self.queryset)
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