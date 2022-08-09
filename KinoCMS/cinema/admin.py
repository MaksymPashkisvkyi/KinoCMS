from django.contrib import admin
from .models import CinemaModel, SEOModel, GalleryModel, HallModel, FilmModel, SessionModel, TicketModel


@admin.register(SEOModel)
class SEOAdmin(admin.ModelAdmin):
    pass


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(CinemaModel)
class CinemaAdmin(admin.ModelAdmin):
    pass


@admin.register(HallModel)
class HallAdmin(admin.ModelAdmin):
    pass


@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(SessionModel)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(TicketModel)
class TicketAdmin(admin.ModelAdmin):
    pass
