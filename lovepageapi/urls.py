from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('usuarios/', include('usuario.urls')),
    path('features/', include('features.urls')),
    path('notes/', include('chat.urls')),
]