from rest_framework import serializers

from .models import Game, Round


class GameSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    tournament_name = serializers.CharField(source="tournament.name", read_only=True)
    round_name = serializers.CharField(source="round.name", read_only=True)
    location = serializers.CharField()
    team_score_info = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ["id", "name", "tournament_name", "round_name", "location", "team_score_info"]

    def get_team_score_info(self, obj):
        return obj.get_team_score_detail()


class ScoreBoardSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    team_score_info = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ["id", "name", "round", "team_score_info"]

    def get_team_score_info(self, obj):
        return obj.get_team_scores()
    

class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ["id", "name"]