from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Game
from .serializer import GameSerializer


class GameListViewSet(viewsets.ViewSet):
    queryset = Game.objects.all()

    def list(self, request):
        tournament = request.query_params.get("tournament")
        if tournament:
            self.queryset = self.queryset.filter(round__tournament=tournament)

        serializer = GameSerializer(self.queryset, many=True)
        return Response(serializer.data)
