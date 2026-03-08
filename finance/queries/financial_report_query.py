from django.db.models import Sum

from finance.models.transaction import Transaction


class FinancialReportQuery:

    @staticmethod
    def total_income(user):

        return (
            Transaction.objects.filter(
                user=user,
                type=Transaction.Type.INCOME,
            ).aggregate(total=Sum("amount"))["total"]
            or 0
        )

    @staticmethod
    def total_expense(user):

        return (
            Transaction.objects.filter(
                user=user,
                type=Transaction.Type.EXPENSE,
            ).aggregate(total=Sum("amount"))["total"]
            or 0
        )

    @staticmethod
    def balance(user):

        income = FinancialReportQuery.total_income(user)
        expense = FinancialReportQuery.total_expense(user)

        return income - expense