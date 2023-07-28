from django.urls import path

from . import views

urlpatterns = [  
    path('<str:search_term>/', views.get_movies)
]