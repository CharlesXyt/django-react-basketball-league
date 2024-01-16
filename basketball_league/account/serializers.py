from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from .models import Account, Role, Team


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    player_match_info = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ["name", "role", "team", "email", "player_match_info"]

    def get_player_match_info(self, obj):
        return obj.get_player_match_info()

    def get_team(self, obj):
        team_instance = obj.team
        if team_instance:
            return {"id": team_instance.id, "name": team_instance.name}
        else:
            return None


class TeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    members = AccountSerializer(many=True)
    coach = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["id", "name", "members", "coach"]

    def get_coach(self, obj):
        coach = obj.get_team_coach()
        return {"id": coach.id, "name": coach.name}


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        token["example"] = "example"

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user_id"] = self.user.id
        return data


class JWTCookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get(settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"])

        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken("No valid refresh token found")
