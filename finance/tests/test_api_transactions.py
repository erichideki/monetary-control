import pytest
from decimal import Decimal
from finance.models.transaction import Transaction
from finance.services.transaction_service import TransactionService

pytestmark = pytest.mark.django_db

def test_create_expense_api(api_client_with_jwt, account, category):
    client, user = api_client_with_jwt
    payload = {
        "account": account.id,
        "category": category.id,
        "amount": "50.00",
        "type": Transaction.Type.EXPENSE.value,
        "description": "Mercado"
    }
    response = client.post("/api/transactions/", payload, format="json")
    assert response.status_code == 201
    assert "id" in response.data

def test_create_income_api(api_client_with_jwt, account, category):
    client, user = api_client_with_jwt
    payload = {
        "account": account.id,
        "category": category.id,
        "amount": "1000.00",
        "type": Transaction.Type.INCOME.value,
        "description": "Salário"
    }
    response = client.post("/api/transactions/", payload, format="json")
    assert response.status_code == 201
    assert "id" in response.data

def test_transaction_report_api(api_client_with_jwt, account, category):
    client, user = api_client_with_jwt
    expense = TransactionService.create_expense(
        user=user, account=account, category=category, amount=Decimal("50.00"), description="Mercado"
    )
    income = TransactionService.create_income(
        user=user, account=account, category=category, amount=Decimal("1000.00"), description="Salário"
    )
    response = client.get("/api/transactions/report/")
    assert response.status_code == 200
    ids = [t["id"] for t in response.data]
    assert expense.id in ids
    assert income.id in ids