from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=255, default="")

    player='Player'
    coach = 'Coach'
    league_admin = 'League Admin'

    def __str__(self):
        return self.name


class Account(AbstractUser):
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=25, default="")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

    def __str__(self):
        return self.name
