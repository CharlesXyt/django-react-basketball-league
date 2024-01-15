from django.urls import path

from .views import GameListViewSet

urlpatterns = [
    path("api/game", GameListViewSet.as_view())
]