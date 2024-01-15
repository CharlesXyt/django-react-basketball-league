from django.urls import path

from .views import (AccountView, JWTCookieTokenObtainPairView,
                    JWTCookieTokenRefreshView, TeamView)

urlpatterns = [
    path("api/token", JWTCookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", JWTCookieTokenRefreshView.as_view(), name="token_refresh"),
    path("api/account", AccountView.as_view()),
    path("api/team", TeamView.as_view())
]