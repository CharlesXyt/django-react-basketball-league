from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from game.views import GameListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/game", GameListViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/schema/ui/", SpectacularSwaggerView.as_view()),
] + router.urls
