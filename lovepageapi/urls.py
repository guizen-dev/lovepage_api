from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path(str(os.getenv('API_KEY'))+'/admin/', admin.site.urls),
    path(str(os.getenv('API_KEY'))+'api-auth/', include('rest_framework.urls')),
    path(str(os.getenv('API_KEY'))+'usuarios/', include('usuario.urls')),
    path(str(os.getenv('API_KEY'))+'features/', include('features.urls')),
    path(str(os.getenv('API_KEY'))+'notes/', include('chat.urls')),
]