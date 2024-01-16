def generate_match(teams):
    matches = []
    random.shuffle(teams)
    for i in range(0, len(teams), 2):
        matches.append([teams[i], teams[i+1]])
    return matches

def create_fake_team_users(fake):
    player_role = Role.objects.get(name='Player')
    coach_role = Role.objects.get(name='Coach')
    league_admin_role = Role.objects.get(name='League Admin')
    Account.objects.exclude(username='admin').delete()
    Team.objects.all().delete()
    Game.objects.all().delete()

    league_admin = Account.objects.create(
        username='league_admin',
        name='league_admin',
        email='league_admin_role_id' + '@email.com',
        role=league_admin_role
    )
    league_admin.set_password('12345')
    league_admin.save()
    for _ in range(16):
        team = Team.objects.create(
            name=fake.user_name() + '_team',
        )
        coach_name = team.name + '_coach'
        coach = Account.objects.create(
            username=coach_name,
            name=coach_name,
            email=coach_name + '@email.com',
            role=coach_role,
            team=team
        )
        coach.set_password('12345')
        coach.save()


        for _ in range(10):
            name = fake.user_name()
            player = Account.objects.create(
                username=name,
                name=name,
                email=name + '@email.com',
                role=player_role,
                team=team
            )
            player.set_password('12345')
            player.save()

def create_tournament(fake):
    Tournament.objects.all().delete()
    tournament = Tournament.objects.create(
        name=fake.sentence(nb_words=2) + ' touranment'
    )
    teams_left = [team for team in Team.objects.prefetch_related('members').all()]
    round_names = ["First Round", "Second Round", "Semi Final", "Final"]
    current_round = 0
    while len(teams_left) > 1:

        matches = generate_match(teams_left)
        teams_left = []
        round_obj = Round.objects.create(
            name=round_names[current_round],
            tournament=tournament
        )
        current_round += 1
        for team_1, team_2 in matches:
            game = Game.objects.create(
                name=team_1.name + ' vs ' + team_2.name,
                round=round_obj,
                location=fake.sentence(nb_words=1) + ' location'
            )
            team_1_player = [(member, random.randint(0, 4)) for member in team_1.members.all() if member.role.name == Role.player]
            team_2_player = [(member, random.randint(0, 4)) for member in team_2.members.all() if member.role.name == Role.player]
            score_team1 = 0
            score_team2 = 0
            for player, score in team_1_player:
                GamePlayerAssociation.objects.create(
                    game=game,
                    player=player,
                    score=score
                )
                score_team1 += score
            for player, score in team_2_player:
                GamePlayerAssociation.objects.create(
                    game=game,
                    player=player,
                    score=score
                )
                score_team2 += score
            GameTeamAssociation.objects.create(
                game=game,
                team=team_1,
                score=score_team1
            )
            GameTeamAssociation.objects.create(
                game=game,
                team=team_2,
                score=score_team2
            )
            winner = team_1 if score_team1 > score_team2 else team_2
            teams_left.append(winner)

def main():
    fake: Faker = Faker()
    # create_fake_team_users(fake)
    create_tournament(fake)
 
if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketball_league.settings")
    application = get_wsgi_application()

    import random

    from account.models import Account, Role, Team
    from faker import Faker
    from game.models import (Game, GamePlayerAssociation, GameTeamAssociation,
                             Round, Tournament)
 
    main()