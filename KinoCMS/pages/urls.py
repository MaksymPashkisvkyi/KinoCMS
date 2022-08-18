from django.urls import path

from .views import MainPageView, PosterView, SoonView, ScheduleView, CinemasView, PromoView, ContactsView, CafeView, \
    MobileAppsView, AdvertisementView, AboutView, NewsView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('poster/', PosterView.as_view(), name='poster'),
    path('soon/', SoonView.as_view(), name='soon'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('cinemas/', CinemasView.as_view(), name='cinemas'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('cafe/', CafeView.as_view(), name='cafe'),
    path('mobile_apps/', MobileAppsView.as_view(), name='mobile_apps'),
    path('advertisement/', AdvertisementView.as_view(), name='advertisement'),
    path('about/', AboutView.as_view(), name='about'),
    path('promo/', PromoView.as_view(), name='promo'),
    path('news/', NewsView.as_view(), name='news'),
]
