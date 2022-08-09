from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'nickname', 'email', 'address', 'gender', 'phone', 'date', 'city']
    list_display_links = ['name']
