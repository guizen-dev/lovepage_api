from rest_framework.generics import ListAPIView
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import permissions

# Create your views here.

class UsuarioView(ListAPIView):
    queryset = Usuario.objects.order_by('id')
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.AllowAny, )