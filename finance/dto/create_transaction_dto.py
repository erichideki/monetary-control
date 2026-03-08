from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateTransactionDTO:

    user: object
    account: object
    category: object
    amount: Decimal
    transaction_type: str
    description: str = ""