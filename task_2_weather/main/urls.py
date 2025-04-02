from django.urls import path
from main import views
from django.conf.urls.static import static

from config import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:city_name>/', views.main, name='city_name')
]
