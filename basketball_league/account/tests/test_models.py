from account.factory.account_factory import AccountFactory, RoleFactory, TeamFactory
from account.models import Role
from django.test import TestCase
from game.factory.game_factory import GameFactory, GamePlayerAssociationFactory


class TeamModelTest(TestCase):
    def setUp(self):
        # Create test objects
        player_role = RoleFactory(name=Role.player)
        coach_role = RoleFactory(name=Role.coach)
        self.team = TeamFactory()
        self.player_user = AccountFactory(role=player_role, team=self.team)
        self.coach_user = AccountFactory(role=coach_role, team=self.team)

    def test_get_team_coach(self):
        # Test if the get_team_coach method returns the correct coach account
        coach_account = self.team.get_team_coach()
        self.assertEqual(coach_account, self.coach_user)


class AccountModelTest(TestCase):
    def setUp(self):
        self.player = AccountFactory(role=RoleFactory(name=Role.player))
        GamePlayerAssociationFactory(game=GameFactory(), player=self.player, score=2)
        GamePlayerAssociationFactory(game=GameFactory(), player=self.player, score=10)

    def test_get_player_match_info(self):
        match_info = self.player.get_player_match_info()
        self.assertEqual(match_info.get("average_score"), 6)
        self.assertEqual(match_info.get("game_count"), 2)
