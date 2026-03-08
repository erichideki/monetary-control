class FinanceDomainError(Exception):
    """Base exception for finance domain"""


class InvalidTransactionAmount(FinanceDomainError):
    """Raised when transaction amount is invalid"""


class InvalidTransactionType(FinanceDomainError):
    """Raised when transaction type is invalid"""