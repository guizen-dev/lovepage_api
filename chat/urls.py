from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('reclamacao/', views.ReclamacaoListView.as_view(), name='list-reclamacao'),
    path('delete_reclamacao/<str:reclamacao_id>', views.ReclamacaoAPIView.delete_chat),
    path('chat/', views.ChatReclamacaoListView.as_view(), name='list-chat'),
    path('delete_chat/<str:chat_id>', views.ChatReclamacaoAPIView.delete_chat)
    #url(r'^(P<id>\d+)/edit/$', views.ReclamacaoUpdateView.as_view())
]