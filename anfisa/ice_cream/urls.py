from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список мороженого
    path('ice_cream/', views.ice_cream_list),
    # Подробная информация о мороженом. Ждем пременную типа int,
    # и будем использовать ее под именем pk
    path(
        'ice_cream/<int:pk>/',
        views.ice_cream_detail
    ),
]
