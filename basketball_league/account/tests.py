from django.test import RequestFactory, TestCase

from .factory.account_factory import AccountFactory
from .models import Role
from .permissions import IsCoach, IsCoachOrLeagueAdmin, IsLeagueAdmin


class PermissionsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.player_user = AccountFactory.create_with_role(Role.player)
        self.coach_user = AccountFactory.create_with_role(Role.coach)
        self.league_admin_user = AccountFactory.create_with_role(Role.league_admin)

        # Create a request object
        self.request = self.factory.get('/')

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