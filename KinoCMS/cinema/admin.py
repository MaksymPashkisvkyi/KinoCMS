from django.contrib import admin
from .models import CinemaModel, SEOModel, GalleryModel, HallModel, FilmModel, SessionModel, BannerConfigModel, \
    PagesModel, TicketModel, BackgroundBannerModel, MainPageModel, BannerMainPageModel, NewsPromoModel, \
    BannerNewsPromoModel, ContactsModel


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
