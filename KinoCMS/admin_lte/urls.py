from django.urls import path
from .views import admin_statistic, AdminCinemaView

urlpatterns = [
    path('', admin_statistic, name='admin_statistic'),
    path('admin_cinema/', AdminCinemaView.as_view(), name='admin_cinema')
]
