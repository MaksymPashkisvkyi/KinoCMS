from django.contrib import admin

from .models import BannerConfigModel, MainPageBannerModel, BackgroundBannerModel, NewsPromoBannerModel


@admin.register(BannerConfigModel)
class BannerConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active', 'rotation_speed']
    list_display_links = ['name']


@admin.register(BackgroundBannerModel)
class BackgroundBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'color', 'is_image', 'config']
    list_display_links = ['image']


@admin.register(MainPageBannerModel)
class BannerMainPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'URL', 'text']
    list_display_links = ['image']


@admin.register(NewsPromoBannerModel)
class BannerNewsPromoAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'URL']
    list_display_links = ['image']
