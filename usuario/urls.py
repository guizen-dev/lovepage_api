from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('register', views.RegisterView.as_view()),
    #path('login', views.LoginView.as_view()),
    path('list', views.all_users),
    path('delete/<str:usuario_id>', views.DeleteView.as_view()),
    path('login', obtain_auth_token, name="login")
]