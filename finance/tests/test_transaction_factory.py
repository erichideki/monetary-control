import pytest
from decimal import Decimal

from finance.services.transaction_service import TransactionService
from finance.tests.factories.user_factory import UserFactory
from finance.tests.factories.account_factory import AccountFactory
from finance.tests.factories.category_factory import CategoryFactory


@pytest.mark.django_db
def test_create_expense_transaction():

    user = UserFactory()
    account = AccountFactory(user=user)
    category = CategoryFactory(type="expense")

    transaction = TransactionService.create_expense(
        user=user,
        account=account,
        category=category,
        amount=Decimal("50.00"),
        description="Dinner"
    )

    assert transaction.amount == Decimal("50.00")