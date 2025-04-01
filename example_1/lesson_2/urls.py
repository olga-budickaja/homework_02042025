from django.urls import path
from lesson_2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:year>/', views.year_archive),
    path('home/', views.home, name='home-view'),
    path('book/', views.book, name='book'),
    path('book/<str:title>/', views.book, name='book'),
    # path('index/', views.index, name='index-view'),
    path('bio/<str:username>/', views.bio, name='bio'),
]
