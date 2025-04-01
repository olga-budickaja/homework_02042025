from django.urls import path
from lesson_1 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index-view'),
    path('bio/', views.bio, name=''),
    path('bio/<str:username>/', views.bio, name='bio')
]
