from account.factory.account_factory import (AccountFactory, RoleFactory,
                                             TeamFactory)
from account.models import Account, Role, Team
from django.test import TestCase


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
