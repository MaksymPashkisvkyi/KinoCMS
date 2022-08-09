from django.contrib import admin

from .models import BannerConfigModel, BannerMainPageModel, BackgroundBannerModel, BannerNewsPromoModel


@admin.register(BannerConfigModel)
class BannerConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(BackgroundBannerModel)
class BackgroundBannerAdmin(admin.ModelAdmin):
    pass


@admin.register(BannerMainPageModel)
class BannerMainPageAdmin(admin.ModelAdmin):
    pass


@admin.register(BannerNewsPromoModel)
class BannerNewsPromoAdmin(admin.ModelAdmin):
    pass
