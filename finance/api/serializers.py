from rest_framework import serializers
from finance.models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            "id",
            "account",
            "category",
            "amount",
            "type",
            "description",
            "created_at",
        ]