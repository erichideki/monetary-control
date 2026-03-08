from rest_framework import serializers
from finance.models.transaction import Transaction
from finance.models.account import Account
from finance.models.category import Category

class CreateTransactionSerializer(serializers.Serializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    type = serializers.ChoiceField(choices=[(Transaction.Type.INCOME.value, "Income"),
                                             (Transaction.Type.EXPENSE.value, "Expense")])
    description = serializers.CharField(max_length=255, required=False, allow_blank=True)