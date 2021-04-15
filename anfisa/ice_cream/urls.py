from django.urls import path
from . import views

# Эта строчка обязательна. 
# Без нее чуда не произойдет и namespace работать не будет
app_name = 'ice_cream'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Список мороженого
    path('ice_cream/', views.icecream_list, name='icecream_list'),
    # Подробная информация о мороженом. Ждем пременную типа int, 
    # и будем использовать ее под именем pk
    path('ice_cream/<int:pk>/', views.icecream_detail, name='icecream_detail'),
]