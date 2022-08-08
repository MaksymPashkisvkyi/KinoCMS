from django.contrib import admin
from .models import CinemaModel, SEOModel, GalleryModel


@admin.register(CinemaModel)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(SEOModel)
class SEOAdmin(admin.ModelAdmin):
    list_display = ('URL',)


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image',)
