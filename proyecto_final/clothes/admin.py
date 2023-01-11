from django.contrib import admin
from clothes.models import *


admin.site.register (Clothes)
admin.site.register (Gender)
admin.site.register (Type_Clothing)

class ClothesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'category', 'gender')
    search_fields = ('category')
    list_filter = ('stock')

    