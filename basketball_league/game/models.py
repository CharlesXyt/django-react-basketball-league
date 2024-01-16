from account.models import Account, Team
from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Round(models.Model):
    name = models.CharField(max_length=255, default="")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    def get_game_count(self):
        return self.game_set.count()

class Game(models.Model):
    name = models.CharField(max_length=255, default="")
    round = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=255, default="")
    teams = models.ManyToManyField(Team, through="GameTeamAssociation")
    players = models.ManyToManyField(Account, through="GamePlayerAssociation")
    tournament = models.OneToOneField("Tournament", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    def get_team_scores(self):
        team_scores = []
        for team_assoc in self.gameteamassociation_set.all():
            team = team_assoc.team
            team_scores.append({"score": team_assoc.score, "team_id": team.id, "name": team.name, "is_winner": False})

        winner_team = max(team_scores, key=lambda x: x["score"])
        winner_team["is_winner"] = True
        return team_scores

    def get_team_score_detail(self):
        team_scores = []
        for team_assoc in self.gameteamassociation_set.all():
            team = team_assoc.team
            team_scores.append({
                "score": team_assoc.score, "team_id": team.id, "name": team.name, 
                "players": self.get_player_detail(team_assoc.team)}
                )
        return team_scores

    def get_player_detail(self, team):
        players = []
        for player_assoc in self.gameplayerassociation_set.filter(player__team=team):
            player = player_assoc.player
            players.append({"score": player_assoc.score, "player_id": player.id, "name": player.username})
        return players


class GameTeamAssociation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.game) + "-" + str(self.team)


class GamePlayerAssociation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Account, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.game) + "-" + str(self.player)
