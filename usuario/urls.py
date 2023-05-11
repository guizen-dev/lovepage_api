from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from . import views

urlpatterns = [
    path('', views.usuario_list),
    path('<str:usuario_id>', views.usuario_detail)
]