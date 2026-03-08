from django.contrib import admin

from finance.models import (
    Account,
    Category,
    Tag,
    Transaction,
    RecurringTransaction,
)


admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Transaction)
admin.site.register(RecurringTransaction)