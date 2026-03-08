from finance.models.transaction import Transaction


class TransactionRepository:

    @staticmethod
    def create(**kwargs) -> Transaction:
        return Transaction.objects.create(**kwargs)

    @staticmethod
    def get_by_id(transaction_id: int) -> Transaction:
        return Transaction.objects.get(id=transaction_id)

    @staticmethod
    def list_by_user(user):
        return Transaction.objects.filter(user=user)

    @staticmethod
    def delete(transaction: Transaction):
        transaction.delete()