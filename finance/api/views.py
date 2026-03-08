from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from finance.models.transaction import Transaction
from finance.api.serializers import CreateTransactionSerializer, TransactionSerializer
from finance.services.transaction_service import TransactionService

class CreateTransactionAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CreateTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if data["type"] == Transaction.Type.EXPENSE.value:
            transaction = TransactionService.create_expense(
                user=request.user,
                account=data["account"],
                category=data["category"],
                amount=Decimal(data["amount"]),
                description=data.get("description", "")
            )
        else:
            transaction = TransactionService.create_income(
                user=request.user,
                account=data["account"],
                category=data["category"],
                amount=Decimal(data["amount"]),
                description=data.get("description", "")
            )

        return Response({"id": transaction.id}, status=status.HTTP_201_CREATED)


class TransactionReportAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = TransactionService.list_transactions(user=request.user)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)