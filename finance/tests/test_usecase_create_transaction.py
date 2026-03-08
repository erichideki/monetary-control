import pytest
from decimal import Decimal
from finance.services.transaction_service import TransactionService
from finance.models.transaction import Transaction

pytestmark = pytest.mark.django_db

def test_create_transaction_usecase_expense(user, account, category):
    transaction = TransactionService.create_expense(
        user=user,
        account=account,
        category=category,
        amount=Decimal("100.00"),
        description="Teste"
    )
    assert transaction.id is not None
    assert transaction.type == Transaction.Type.EXPENSE.value

def test_create_transaction_usecase_income(user, account, category):
    transaction = TransactionService.create_income(
        user=user,
        account=account,
        category=category,
        amount=Decimal("1000.00"),
        description="Salário"
    )
    assert transaction.id is not None
    assert transaction.type == Transaction.Type.INCOME.value