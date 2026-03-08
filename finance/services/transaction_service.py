from decimal import Decimal
from finance.models.transaction import Transaction
from finance.domain.exceptions import InvalidTransactionAmount

class TransactionService:

    @staticmethod
    def create_income(*, user, account, category, amount: Decimal, description=""):
        if amount <= 0:
            raise InvalidTransactionAmount("Amount must be positive")
        return Transaction.objects.create(
            user=user,
            account=account,
            category=category,
            amount=amount,
            type=Transaction.Type.INCOME,
            description=description
        )

    @staticmethod
    def create_expense(*, user, account, category, amount: Decimal, description=""):
        if amount <= 0:
            raise InvalidTransactionAmount("Expense amount must be positive")
        return Transaction.objects.create(
            user=user,
            account=account,
            category=category,
            amount=amount,
            type=Transaction.Type.EXPENSE,
            description=description
        )

    @staticmethod
    def list_transactions(user):
        return Transaction.objects.filter(user=user)