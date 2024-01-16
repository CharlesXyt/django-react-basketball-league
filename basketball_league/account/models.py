from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

    def get_team_coach(self):
        coach_account = Account.objects.filter(team=self, role__name="Coach").first()
        return coach_account


class Role(models.Model):
    name = models.CharField(max_length=255, default="")

    player = "Player"
    coach = "Coach"
    league_admin = "League Admin"

    def __str__(self):
        return self.name


class Account(AbstractUser):
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=25, default="")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="members")

    def __str__(self):
        return self.name

    def get_player_match_info(self):
        from game.models import GamePlayerAssociation

        game_player_associations = GamePlayerAssociation.objects.filter(player=self)
        if game_player_associations.exists():
            total_score = sum(association.score for association in game_player_associations)
            return {
                "average_score": round(total_score / len(game_player_associations), 2),
                "game_count": len(game_player_associations),
            }
        return {"average_score": 0, "game_count": 0}
