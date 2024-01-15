from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game
from .serializer import GameSerializer


class GameListViewSet(APIView):
    queryset = Game.objects.all()

    def get(self, request):
        tournament = request.query_params.get("tournament")
        if tournament:
            self.queryset = self.queryset.filter(round__tournament=tournament)

        serializer = GameSerializer(self.queryset, many=True)
        return Response(serializer.data)
