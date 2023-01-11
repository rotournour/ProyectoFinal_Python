from django.contrib import admin
from sales.models import Payment, Sales

admin.site.register (Payment)
admin.site.register (Sales)

class SalesAdmin(admin.ModelAdmin):
    list_display = ('client', 'clothes_name', 'creation_time', 'payment')