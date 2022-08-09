from django.contrib import admin
from .models import MainPageModel, PagesModel, ContactsModel, NewsPromoModel


@admin.register(MainPageModel)
class MainPageAdmin(admin.ModelAdmin):
    pass


@admin.register(PagesModel)
class PagesAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsModel)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsPromoModel)
class NewsPromoAdmin(admin.ModelAdmin):
    pass
