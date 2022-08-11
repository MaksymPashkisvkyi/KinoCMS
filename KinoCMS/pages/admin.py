from django.contrib import admin
from .models import MainPageModel, PageModel, ContactModel, NewsPromoModel


@admin.register(MainPageModel)
class MainPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_phone', 'second_phone']


@admin.register(PageModel)
class PagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['name']


@admin.register(ContactModel)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'coords']
    list_display_links = ['name']


@admin.register(NewsPromoModel)
class NewsPromoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'date']
    list_display_links = ['name']
