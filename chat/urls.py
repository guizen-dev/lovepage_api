from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    re_path('reclamacao/', views.ReclamacaoListView.as_view()),
    re_path('chat/', views.ChatReclamacaoListView.as_view()),
    #url(r'^(P<id>\d+)/edit/$', views.ReclamacaoUpdateView.as_view())
]