import factory
from account.models import Account, Role


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')

    @classmethod
    def create_with_role(cls, role_name):
        user = cls()
        user.save()

        role, created = Role.objects.get_or_create(name=role_name)
        user.role = role
        user.save()
        return user
