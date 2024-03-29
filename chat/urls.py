from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [  
    path('', views.notes_list),
    path('chats/', views.chat_note_list),
    path('chats/<str:chat_id>/', views.chat_notes_detail),
    path('<str:note_id>/', views.notes_detail),
    path('chats/note/<str:note_id>/', views.messages_note)
]