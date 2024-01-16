import factory
from account.factory.account_factory import AccountFactory, TeamFactory
from game.models import (Game, GamePlayerAssociation, GameTeamAssociation,
                         Round, Team, Tournament)


class TournamentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tournament

    name = factory.Faker('word')

class RoundFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Round

    name = factory.Faker('word')
    tournament = factory.SubFactory(TournamentFactory)


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Faker('word')
    round = factory.SubFactory(RoundFactory)
    location = factory.Faker('city')
    tournament = factory.SubFactory(TournamentFactory)

class GameTeamAssociationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameTeamAssociation

    game = factory.SubFactory(GameFactory)
    team = factory.SubFactory(TeamFactory)
    score = factory.Faker('random_int', min=0, max=100)

class GamePlayerAssociationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GamePlayerAssociation

    game = factory.SubFactory(GameFactory)
    player = factory.SubFactory(AccountFactory)
    score = factory.Faker('random_int', min=0, max=100)