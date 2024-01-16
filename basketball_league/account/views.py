from django.conf import settings
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .models import Account, Role, Team
from .permissions import IsCoachOrLeagueAdmin
from .serializers import (AccountSerializer, CustomTokenObtainPairSerializer,
                          JWTCookieTokenRefreshSerializer, TeamSerializer)

# Create your views here.


class AccountView(APIView):
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        user_id = request.query_params.get("user_id")

        if user_id and user_id != current_user.id:
            if current_user.role.name == Role.player:
                raise PermissionDenied("You cannot access other user information")
            elif current_user.role.name == Role.coach:
                self.queryset = self.queryset.filter(team__id=current_user.team.id, id=user_id).first()
                if not self.queryset:
                    raise PermissionDenied("You cannot access this user information")
            else:
                self.queryset = self.queryset.get(id=user_id)
        else:
            self.queryset = self.queryset.get(id=current_user.id)

        serializer = AccountSerializer(self.queryset)
        return Response(serializer.data)


class TeamView(APIView):
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated, IsCoachOrLeagueAdmin]

    def get(self, request):
        current_user = request.user
        team_id = int(request.query_params.get("team_id"))

        if current_user.role.name == Role.league_admin:
            self.queryset = self.queryset.get(id=team_id)
        elif not team_id or team_id == current_user.team.id:
            self.queryset = self.queryset.get(id=current_user.team.id)
        else:
            raise PermissionDenied("You cannot access other team information")

        serializer = TeamSerializer(self.queryset)
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
