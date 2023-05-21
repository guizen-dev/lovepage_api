from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.all_features),
    path('type/<str:feature_type>', views.type_features),
    path('detail/<str:feature_id>/', views.feature_detail)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)