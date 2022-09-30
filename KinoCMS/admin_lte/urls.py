from django.urls import path

from .views import (AddUserView,
                    AdminCinemaView, AdminFilmView,
                    AdminUserView, DeleteCinemaView, DeleteFilmView,
                    DeleteHallView, DeleteUserView,
                    EditUserView, admin_statistic, add_cinema_view, add_film_view, add_hall_view,
                    edit_cinema_view, edit_film_view, edit_hall_view, banners_view, AdminPageView, add_page_view,
                    edit_page_view, DeletePageView, edit_main_page_view, edit_contact_view, add_article_view,
                    edit_article_view, AdminArticleView, DeleteArticleView)

urlpatterns = [
    path('', admin_statistic, name='admin_statistic'),

    path('banners/', banners_view, name='admin_banner'),

    path('cinemas/', AdminCinemaView.as_view(), name='admin_cinema'),
    path('cinema/add/', add_cinema_view, name='admin_add_cinema'),
    path('cinema/<int:pk>/', edit_cinema_view, name='admin_edit_cinema'),
    path('cinema/delete/<int:pk>/', DeleteCinemaView.as_view(), name='admin_delete_cinema'),

    path('cinema/<int:pk>/hall/add/', add_hall_view, name='admin_add_hall'),
    path('hall/<int:pk>/', edit_hall_view, name='admin_edit_hall'),
    path('hall/delete/<int:pk>/', DeleteHallView.as_view(), name='admin_delete_hall'),

    path('users/', AdminUserView.as_view(), name='admin_user'),
    path('user/add/', AddUserView.as_view(), name='admin_add_user'),
    path('user/<int:pk>/', EditUserView.as_view(), name='admin_edit_user'),
    path('user/delete/<int:pk>/', DeleteUserView.as_view(), name='admin_delete_user'),

    path('films/', AdminFilmView.as_view(), name='admin_film'),
    path('film/add/', add_film_view, name='admin_add_film'),
    path('film/<int:pk>/', edit_film_view, name='admin_edit_film'),
    path('film/delete/<int:pk>/', DeleteFilmView.as_view(), name='admin_delete_film'),

    path('pages/', AdminPageView.as_view(), name='admin_pages'),
    path('page/add/', add_page_view, name='admin_add_page'),
    path('page/<int:pk>/', edit_page_view, name='admin_edit_page'),
    path('page/delete/<int:pk>/', DeletePageView.as_view(), name='admin_delete_page'),

    path('page/main/<int:pk>/', edit_main_page_view, name='admin_edit_main_page'),
    path('contacts/', edit_contact_view, name='admin_edit_contact'),

    path('promo/', AdminArticleView.as_view(), name='admin_promo'),
    path('promo/add/', add_article_view, name='admin_add_promo'),
    path('promo/<int:pk>/', edit_article_view, name='admin_edit_article'),
    path('promo/delete/<int:pk>/', DeleteArticleView.as_view(), name='admin_delete_article'),

    path('news/', AdminArticleView.as_view(), name='admin_news'),
    path('news/add/', add_article_view, name='admin_add_news'),
    path('news/<int:pk>/', edit_article_view, name='admin_edit_article'),
    path('news/delete/<int:pk>/', DeleteArticleView.as_view(), name='admin_delete_article'),
]
