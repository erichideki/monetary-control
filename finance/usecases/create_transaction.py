from finance.dto.create_transaction_dto import CreateTransactionDTO
from finance.services.transaction_service import TransactionService
from finance.domain.exceptions import InvalidTransactionType


class CreateTransactionUseCase:

    def execute(self, dto: CreateTransactionDTO):

        if dto.transaction_type == "income":
            return TransactionService.create_income(
                user=dto.user,
                account=dto.account,
                category=dto.category,
                amount=dto.amount,
                description=dto.description,
            )

        if dto.transaction_type == "expense":
            return TransactionService.create_expense(
                user=dto.user,
                account=dto.account,
                category=dto.category,
                amount=dto.amount,
                description=dto.description,
            )

        raise InvalidTransactionType()