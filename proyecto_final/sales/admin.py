from django.contrib import admin
from sales.models import Payment



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('choices',)