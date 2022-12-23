from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('filme', views.FilmeView.as_view()),
    path('lugar', views.LugarView.as_view()),
    path('mural', views.MuralView.as_view()),
    path('jogo', views.JogoView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)