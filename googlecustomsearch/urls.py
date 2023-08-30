from django.urls import path

from . import views

urlpatterns = [  
    path('search/<str:search_term>/', views.search_photo)
]