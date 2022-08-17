from django.urls import path
from .views import admin_statistic, AdminCinemaView, AdminGalleryView, AdminSessionView, AdminTicketView, AdminFilmView, \
    AdminUserView, AdminHallView, AdminSEOView, AdminBackgroundBannerView, AdminMainPageBannerView, \
    AdminNewsPromoBannerView, AdminBannerConfigView, AdminBannerView

urlpatterns = [
    path('', admin_statistic, name='admin_statistic'),
    path('admin_cinema/', AdminCinemaView.as_view(), name='admin_cinema'),
    path('admin_film/', AdminFilmView.as_view(), name='admin_film'),
    path('admin_hall/', AdminHallView.as_view(), name='admin_hall'),
    path('admin_session/', AdminSessionView.as_view(), name='admin_session'),
    path('admin_ticket/', AdminTicketView.as_view(), name='admin_ticket'),
    path('admin_user/', AdminUserView.as_view(), name='admin_user'),
    path('admin_SEO/', AdminSEOView.as_view(), name='admin_SEO'),
    path('admin_gallery/', AdminGalleryView.as_view(), name='admin_gallery'),
    path('admin_banner/', AdminBannerView.as_view(), name='admin_banner'),
    path('admin_background_banner/', AdminBackgroundBannerView.as_view(), name='admin_background_banner'),
    path('admin_new_promo_banner/', AdminNewsPromoBannerView.as_view(), name='admin_new_promo_banner'),
    path('admin_main_page_banner/', AdminMainPageBannerView.as_view(), name='admin_main_page_banner'),
    path('admin_banner_config/', AdminBannerConfigView.as_view(), name='admin_banner_config'),
]
