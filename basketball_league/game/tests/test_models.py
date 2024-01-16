from account.factory.account_factory import AccountFactory, TeamFactory
from django.test import TestCase
from game.factory.game_factory import (GameFactory, GameTeamAssociationFactory,
                                       RoundFactory, TournamentFactory)


class RoundModelTest(TestCase):
    def setUp(self):
        self.round = RoundFactory()
        GameFactory(round=self.round)
        GameFactory(round=self.round)

    def test_get_game_count(self):
        self.round.get_game_count()
        self.assertEqual(self.round.get_game_count(), 2)

class GameModelTest(TestCase):
    def setUp(self):
        # Create test objects
        self.round_instance = RoundFactory(tournament=TournamentFactory())

        self.team_1 = TeamFactory()
        self.team_2 = TeamFactory()
        self.game = GameFactory()
        
        GameTeamAssociationFactory(team=self.team_1, game=self.game, score=5)
        GameTeamAssociationFactory(team=self.team_2, game=self.game, score=6)


    def test_get_team_scores(self):
        team_scores = self.game.get_team_scores()
        self.assertEqual(len(team_scores), 2)
        for team_score in team_scores:
            if team_score.get("team_id") == self.team_1.id:
                self.assertEqual(team_score.get("score"), 5) 
                self.assertEqual(team_score.get("is_winner"), False)
            else:
                self.assertEqual(team_score.get("score"), 6) 
                self.assertEqual(team_score.get("is_winner"), True)