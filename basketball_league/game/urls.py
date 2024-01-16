from django.urls import path

from .views import GameView, RoundView, ScoreBoardView

urlpatterns = [
    path("api/game", GameView.as_view(), name="game"),
    path("api/scoreboard", ScoreBoardView.as_view(), name="score_board"),
    path("api/round", RoundView.as_view(), name="round")
]
