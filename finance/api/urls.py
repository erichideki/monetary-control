from django.urls import path
from finance.api.views import CreateTransactionAPI, TransactionReportAPI


urlpatterns = [
    path("transactions/", CreateTransactionAPI.as_view(), name="create_transaction"),
    path("transactions/report/", TransactionReportAPI.as_view(), name="transaction_report"),
]