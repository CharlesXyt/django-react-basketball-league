from account.models import Role
from account.permissions import IsCoachOrLeagueAdmin
from django.db.models import Count
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game, Round
from .serializers import GameSerializer, RoundSerializer, ScoreBoardSerializer


class GameView(APIView):
    permission_classes = [IsAuthenticated, IsCoachOrLeagueAdmin]
    queryset = Game.objects.all()

    def get(self, request):
        current_user = request.user
        game_id = int(request.query_params.get("game_id"))
        try:
            game_instance = self.queryset.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=404)

        if current_user.role.name == Role.coach and current_user.team.id not in [
            team.id for team in game_instance.teams.all()
        ]:
            raise PermissionDenied("You cannot access that game info")

        serializer = GameSerializer(game_instance)
        return Response(serializer.data)


class ScoreBoardView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects

    def get(self, request):
        round_id = request.query_params.get('round_id')
        if round_id:
            self.queryset = self.queryset.filter(round=int(round_id))
        serializer = ScoreBoardSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

class RoundView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        round_instance = Round.objects.annotate(game_count=Count('game')).order_by('-game_count')
        serializer = RoundSerializer(round_instance, many=True)
        return Response(serializer.data)
    
