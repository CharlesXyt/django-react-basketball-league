def main():
    fake: Faker = Faker()
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

 
if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basketball_league.settings")
    application = get_wsgi_application()

    from account.models import Account, Role, Team
    from faker import Faker
    from game.models import Game
 
    main()