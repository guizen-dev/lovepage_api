from django.urls import path

from . import views

urlpatterns = [  
    path('search/<str:search_term>/', views.search_games),
    path('detail/<str:game_id>/', views.game_detail),
    path('popular', views.popular_games)
]