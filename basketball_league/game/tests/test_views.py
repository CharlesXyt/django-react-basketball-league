from unittest.mock import patch

from account.factory.account_factory import (AccountFactory, RoleFactory,
                                             TeamFactory)
from account.models import Role
from django.urls import reverse
from game.factory.game_factory import GameFactory, RoundFactory
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class GameViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.game = GameFactory()
        self.other_game = GameFactory()
        self.team_1 = TeamFactory()
        self.team_2 = TeamFactory()
        self.game.teams.add(self.team_1, self.team_2)
        self.coach_user = AccountFactory(role=RoleFactory(name=Role.coach), team=self.team_1)
        self.league_admin_user = AccountFactory(role=RoleFactory(name=Role.league_admin))
        self.api_url = reverse("game")

    def test_game_not_exists(self):
        self.client.force_authenticate(user=self.coach_user)
        response = self.client.get(self.api_url, {'game_id': self.game.id + 10})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_authenticated_coach_view_own_game(self):
        self.client.force_authenticate(user=self.coach_user)
        response = self.client.get(self.api_url, {'game_id': self.game.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_coach_view_other_game(self):
        self.client.force_authenticate(user=self.coach_user)
        response = self.client.get(self.api_url, {'game_id': self.other_game.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_league_admin_view_game(self):
        self.client.force_authenticate(user=self.league_admin_user)
        response = self.client.get(self.api_url, {'game_id': self.game.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ScoreViewTest(APITestCase):
    def setUp(self):

        self.user = AccountFactory(role=RoleFactory(name=Role.player))
        self.client.force_authenticate(user=self.user)


        self.round1 = RoundFactory()
        self.round2 = RoundFactory()
        self.game1 = GameFactory(round=self.round1)
        self.game2 = GameFactory(round=self.round2)

        self.api_url = reverse("score_board")

    @patch('game.serializers.Game.get_team_scores')
    def test_score_board_view_with_round_id(self, mock_get_team_scores):
        
        mock_get_team_scores.return_value = None

        response = self.client.get(self.api_url, {'round_id': self.round1.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].get('id'), self.game1.id)


    @patch('game.serializers.Game.get_team_scores')
    def test_score_board_view_without_round_id(self, mock_get_team_scores):
        mock_get_team_scores.return_value = None
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)