import factory
from account.models import Account, Role, Team


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role

        

class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    name = factory.Faker("name")

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    role = factory.SubFactory(RoleFactory)
    team = factory.SubFactory(TeamFactory)


