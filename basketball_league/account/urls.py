from django.urls import path

from .views import (AccountViewSet, JWTCookieTokenObtainPairView,
                    JWTCookieTokenRefreshView)

urlpatterns = [
    path("api/token", JWTCookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", JWTCookieTokenRefreshView.as_view(), name="token_refresh"),
    path("api/account", AccountViewSet.as_view())
]