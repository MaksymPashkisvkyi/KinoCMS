from django.urls import path
from .views import admin_statistic, AdminCinemaView, AdminFilmView, AdminUserView, AdminBannerView, AddCinemaView, \
    AddHallView, AddUserView, AddFilmView, EditCinemaView, DeleteCinemaView

urlpatterns = [
    path('', admin_statistic, name='admin_statistic'),
    path('cinemas/', AdminCinemaView.as_view(), name='admin_cinema'),
    path('films/', AdminFilmView.as_view(), name='admin_film'),
    path('users/', AdminUserView.as_view(), name='admin_user'),
    path('banners/', AdminBannerView.as_view(), name='admin_banner'),

    path('add_cinema/', AddCinemaView.as_view(), name='admin_add_cinema'),
    path('add_hall/', AddHallView.as_view(), name='admin_add_hall'),
    path('add_user/', AddUserView.as_view(), name='admin_add_user'),
    path('add_film/', AddFilmView.as_view(), name='admin_add_film'),

    path('edit_cinema/<int:pk>/', EditCinemaView.as_view(), name='admin_edit_cinema'),

    path('delete_cinema/<int:pk>/', DeleteCinemaView.as_view(), name='admin_delete_cinema'),

]
