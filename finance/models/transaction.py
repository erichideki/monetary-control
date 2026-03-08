from django.db import models


class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"

    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    account = models.ForeignKey("finance.Account", on_delete=models.CASCADE)
    category = models.ForeignKey("finance.Category", on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    type = models.CharField(
        max_length=10,
        choices=Type.choices,
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)