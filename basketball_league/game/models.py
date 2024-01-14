from account.models import Account, Team
from django.db import models


class Tounament(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Round(models.Model):
    name = models.CharField(max_length=255, default="")
    tournament = models.ForeignKey(Tounament, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255, default="")
    round = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=255, default="")
    teams = models.ManyToManyField(Team, through="GameTeamAssociation")
    players = models.ManyToManyField(Account, through="GamePlayerAssociation")

    def __str__(self):
        return self.name


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
