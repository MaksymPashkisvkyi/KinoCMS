from django.urls import path

from .views import (AddHallView, AddUserView,
                    AdminBannerView, AdminCinemaView, AdminFilmView,
                    AdminUserView, DeleteCinemaView, DeleteFilmView,
                    DeleteHallView, DeleteUserView,
                    EditHallView, EditUserView, admin_statistic, add_cinema_view, add_film_view,
                    edit_cinema_view, edit_film_view)

urlpatterns = [
    path('', admin_statistic, name='admin_statistic'),

    path('banners/', AdminBannerView.as_view(), name='admin_banner'),

    path('cinemas/', AdminCinemaView.as_view(), name='admin_cinema'),
    path('add_cinema/', add_cinema_view, name='admin_add_cinema'),
    path('edit_cinema/<int:pk>/', edit_cinema_view, name='admin_edit_cinema'),
    path('delete_cinema/<int:pk>/', DeleteCinemaView.as_view(), name='admin_delete_cinema'),

    path('users/', AdminUserView.as_view(), name='admin_user'),
    path('add_user/', AddUserView.as_view(), name='admin_add_user'),
    path('edit_user/<int:pk>/', EditUserView.as_view(), name='admin_edit_user'),
    path('delete_user/<int:pk>/', DeleteUserView.as_view(), name='admin_delete_user'),

    path('add_hall/', AddHallView.as_view(), name='admin_add_hall'),
    path('edit_hall/<int:pk>/', EditHallView.as_view(), name='admin_edit_hall'),
    path('delete_hall/<int:pk>/', DeleteHallView.as_view(), name='admin_delete_hall'),

    path('films/', AdminFilmView.as_view(), name='admin_film'),
    path('add_film/', add_film_view, name='admin_add_film'),
    path('edit_film/<int:pk>/', edit_film_view, name='admin_edit_film'),
    path('delete_film/<int:pk>/', DeleteFilmView.as_view(), name='admin_delete_film'),
]
