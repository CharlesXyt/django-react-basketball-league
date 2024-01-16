from account.factory.account_factory import (AccountFactory, RoleFactory,
                                             TeamFactory)
from account.models import Role
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class TeamAPIViewTest(APITestCase):
    def setUp(self):
        self.team = TeamFactory()
        self.other_team = TeamFactory()
        AccountFactory(role=RoleFactory(name=Role.coach), team=self.other_team)
        self.coach = AccountFactory(role=RoleFactory(name=Role.coach), team=self.team)
        self.league_admin = AccountFactory(role=RoleFactory(name=Role.league_admin))

        self.client = APIClient()
        self.api_url = reverse("team")

    def test_authenticated_coach_view_own_team(self):
        self.client.force_authenticate(user=self.coach)
        response = self.client.get(self.api_url, {"team_id": self.team.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_authenticated_coach_view_other_team(self):
        self.client.force_authenticate(user=self.coach)
        response = self.client.get(self.api_url, {"team_id": self.other_team.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_league_admin_view_other_team(self):
        self.client.force_authenticate(user=self.league_admin)
        response = self.client.get(self.api_url, {"team_id": self.other_team.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AccountAPIViewTest(APITestCase):
    def setUp(self):
        self.team = TeamFactory()
        self.player = AccountFactory(role=RoleFactory(name=Role.player), team=self.team)
        self.coach = AccountFactory(role=RoleFactory(name=Role.coach), team=self.team)
        self.league_admin = AccountFactory(role=RoleFactory(name=Role.league_admin))
        self.player_other_team = AccountFactory(role=RoleFactory(name=Role.player), team=TeamFactory())

        self.client = APIClient()
        self.api_url = reverse("account")

    def test_authenticated_player_view_own_account(self):
        self.client.force_authenticate(user=self.player)
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_player_view_other_account(self):
        self.client.force_authenticate(user=self.player)
        response = self.client.get(self.api_url, {"user_id": self.coach.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_coach_view_own_team_player(self):
        self.client.force_authenticate(user=self.coach)
        response = self.client.get(self.api_url, {"user_id": self.player.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_coach_view_other_team_player(self):
        self.client.force_authenticate(user=self.coach)
        response = self.client.get(self.api_url, {"user_id": self.player_other_team.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_league_admin_view_other_team_player(self):
        self.client.force_authenticate(user=self.league_admin)
        response = self.client.get(self.api_url, {"user_id": self.player.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    