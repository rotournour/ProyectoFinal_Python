from django.contrib import admin
from users.models import UserProfile

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'birth_date',)
    search_fields = ('user',)
