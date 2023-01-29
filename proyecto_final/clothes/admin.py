from django.contrib import admin
from clothes.models import Clothes, Gender, Type_Clothing


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'gender', 'payment', 'buyer_username', 'is_available')
    search_fields = ('category',)
    list_filter = ('is_available',)
    
@admin.register(Gender)
class GendersAdmin(admin.ModelAdmin):
    list_display = ('genders',)
    
@admin.register(Type_Clothing)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories',)
