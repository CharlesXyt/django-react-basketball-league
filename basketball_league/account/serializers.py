from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer,
                                                  TokenRefreshSerializer)

from .models import Account, Role, Team


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    average_score = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ["username", "role", "team", "email", "average_score"]

    def get_average_score(self, obj):
        return obj.get_average_score()


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["name", "members"]

    name = serializers.CharField()
    members = AccountSerializer(many=True)


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
