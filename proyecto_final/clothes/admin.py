from django.contrib import admin
from clothes.models import Clothes, Gender, Type_Clothing

admin.site.register (Gender)
admin.site.register (Type_Clothing)

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender', 'is_available')
    search_fields = ('category',)
    list_filter = ('is_available',)