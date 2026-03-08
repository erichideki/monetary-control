import factory
from decimal import Decimal
from finance.models import Transaction
from .user_factory import UserFactory
from .account_factory import AccountFactory
from .category_factory import CategoryFactory

class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    user = factory.SubFactory(UserFactory)
    account = factory.LazyAttribute(lambda obj: AccountFactory(user=obj.user))
    category = factory.LazyAttribute(lambda obj: CategoryFactory(user=obj.user))
    amount = Decimal("100.00")
    type = "EXPENSE"
    description = "Default transaction"