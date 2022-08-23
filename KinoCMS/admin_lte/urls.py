from django.urls import path
from .views import admin_statistic, AdminCinemaView, AdminGalleryView, AdminSessionView, AdminTicketView, AdminFilmView, \
    AdminUserView, AdminSEOView, AdminBackgroundBannerView, AdminMainPageBannerView, \
    AdminNewsPromoBannerView, AdminBannerConfigView, AdminBannerView, AddCinemaView, AddHallView, AddSEOView, \
    AddGalleryView, AddUserView, AddFilmView

urlpatterns = [
    path('', admin_statistic, name='admin_statistic'),
    path('cinemas/', AdminCinemaView.as_view(), name='admin_cinema'),
    path('films/', AdminFilmView.as_view(), name='admin_film'),
    path('sessions/', AdminSessionView.as_view(), name='admin_session'),
    path('tickets/', AdminTicketView.as_view(), name='admin_ticket'),
    path('users/', AdminUserView.as_view(), name='admin_user'),
    path('SEO/', AdminSEOView.as_view(), name='admin_seo'),
    path('galleries/', AdminGalleryView.as_view(), name='admin_gallery'),
    path('banners/', AdminBannerView.as_view(), name='admin_banner'),
    path('background_banners/', AdminBackgroundBannerView.as_view(), name='admin_background_banner'),
    path('new_promo_banners/', AdminNewsPromoBannerView.as_view(), name='admin_new_promo_banner'),
    path('main_page_banners/', AdminMainPageBannerView.as_view(), name='admin_main_page_banner'),
    path('banner_configs/', AdminBannerConfigView.as_view(), name='admin_banner_config'),

    path('add_cinema/', AddCinemaView.as_view(), name='admin_add_cinema'),
    path('add_hall/', AddHallView.as_view(), name='admin_add_hall'),
    path('add_seo/', AddSEOView.as_view(), name='admin_add_seo'),
    path('add_gallery/', AddGalleryView.as_view(), name='admin_add_gallery'),
    path('add_user/', AddUserView.as_view(), name='admin_add_user'),
    path('add_film/', AddFilmView.as_view(), name='admin_add_film'),
]
