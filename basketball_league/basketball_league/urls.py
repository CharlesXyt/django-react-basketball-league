from account.views import (AccountViewSet, JWTCookieTokenObtainPairView,
                           JWTCookieTokenRefreshView)
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from game.views import GameListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/game", GameListViewSet)
router.register("api/user", AccountViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/schema/ui", SpectacularSwaggerView.as_view()),
    path("api/token", JWTCookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", JWTCookieTokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
