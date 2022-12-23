from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('filme/', views.FilmeView.as_view()),
    path('delete_filme/<str:filme_id>', views.FilmeAPIView.delete_filme),
    path('lugar/', views.LugarView.as_view()),
    path('delete_lugar/<str:lugar_id>', views.LugarAPIView.delete_lugar),
    path('mural/', views.MuralView.as_view()),
    path('delete_mural/<str:mural_id>', views.MuralAPIView.delete_mural),
    path('jogo/', views.JogoView.as_view()),
    path('delete_jogo/<str:jogo_id>', views.JogoAPIView.delete_jogo),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)