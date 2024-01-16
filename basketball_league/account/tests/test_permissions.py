from account.factory.account_factory import AccountFactory, RoleFactory
from account.models import Role
from account.permissions import IsCoach, IsCoachOrLeagueAdmin, IsLeagueAdmin
from django.test import RequestFactory, TestCase


class PermissionsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        player_role = RoleFactory(name=Role.player)
        coach_role = RoleFactory(name=Role.coach)
        league_admin_role = RoleFactory(name=Role.league_admin)
        self.player_user = AccountFactory(role=player_role)
        self.coach_user = AccountFactory(role=coach_role)
        self.league_admin_user = AccountFactory(role=league_admin_role)

        # Create a request object
        self.request = self.factory.get("/")

    def test_is_coach_permission(self):
        # Assign the IsCoach permission to the user
        self.request.user = self.coach_user
        is_coach = IsCoach()
        self.assertTrue(is_coach.has_object_permission(self.request))

    def test_is_not_coach_permission(self):
        # Assign a different role to the user
        self.request.user = self.league_admin_user
        is_coach = IsCoach()
        self.assertFalse(is_coach.has_object_permission(self.request))

    def test_is_league_admin_permission(self):
        # Assign the IsLeagueAdmin permission to the user
        self.request.user = self.league_admin_user
        is_league_admin = IsLeagueAdmin()
        self.assertTrue(is_league_admin.has_object_permission(self.request))

    def test_is_not_league_admin_permission(self):
        # Assign a different role to the user
        self.request.user = self.coach_user
        is_league_admin = IsLeagueAdmin()
        self.assertFalse(is_league_admin.has_object_permission(self.request))

    def test_is_coach_or_league_admin_permission_coach(self):
        # Assign the IsCoachOrLeagueAdmin permission to the user with coach role
        self.request.user = self.coach_user
        is_coach_or_league_admin = IsCoachOrLeagueAdmin()
        self.assertTrue(is_coach_or_league_admin.has_object_permission(self.request))

    def test_is_coach_or_league_admin_permission_league_admin(self):
        # Assign the IsCoachOrLeagueAdmin permission to the user with league admin role
        self.request.user = self.league_admin_user
        is_coach_or_league_admin = IsCoachOrLeagueAdmin()
        self.assertTrue(is_coach_or_league_admin.has_object_permission(self.request))

    def test_is_not_coach_or_league_admin_permission(self):
        # Assign a different role to the user
        self.request.user = self.player_user
        is_coach_or_league_admin = IsCoachOrLeagueAdmin()
        self.assertFalse(is_coach_or_league_admin.has_object_permission(self.request))
