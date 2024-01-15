from account.models import Role
from account.permissions import IsCoachOrLeagueAdmin
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game
from .serializer import GameSerializer


class GameListViewSet(APIView):
    permission_classes = [IsAuthenticated, IsCoachOrLeagueAdmin]
    queryset = Game.objects.all()

    def get(self, request):
        current_user = request.user
        game_id = request.query_params.get('game_id')
        try:
            game_instance = self.queryset.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=404)
        
        if (
            current_user.role.name == Role.coach and 
            current_user.team.id not in [team.id for team in game_instance.teams.all()]
        ):
            raise PermissionDenied("You cannot access that game info")

        serializer = GameSerializer(game_instance)
        return Response(serializer.data)
