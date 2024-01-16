from django.urls import path

from .views import GameListViewSet, RoundListViewSet, ScoreBoardListViewSet

urlpatterns = [
    path("api/game", GameListViewSet.as_view()),
    path("api/scoreboard", ScoreBoardListViewSet.as_view()),
    path("api/round", RoundListViewSet.as_view())
]
