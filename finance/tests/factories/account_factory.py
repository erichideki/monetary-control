import factory
from finance.models.account import Account
from .user_factory import UserFactory


class AccountFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)
    name = "Main Account"