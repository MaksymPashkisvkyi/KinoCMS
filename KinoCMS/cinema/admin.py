from django.contrib import admin
from .models import CinemaModel, SEOModel, GalleryModel, HallModel, FilmModel, SessionModel, TicketModel


@admin.register(SEOModel)
class SEOAdmin(admin.ModelAdmin):
    list_display = ['id', 'URL', 'title', 'keywords', 'description']
    list_display_links = ['title']


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['name']


@admin.register(CinemaModel)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'condition']
    list_display_links = ['name']


@admin.register(HallModel)
class HallAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'hall_scheme', 'cinema']
    list_display_links = ['name']


@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'URL', 'three_D', 'two_D', 'IMAX']
    list_display_links = ['name']


@admin.register(SessionModel)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'film', 'hall', 'price', 'time', 'three_D', 'DBOX', 'VIP']
    list_display_links = ['film']


@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'session', 'user', 'seat', 'reservation']
    list_display_links = ['session']
