from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    class Type(models.TextChoices):
        EXPENSE = "EXPENSE", "Expense"
        INCOME = "INCOME", "Income"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=Type.choices)