from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Filme, Lugar, Mural, Jogo
from .serializers import FilmeSerializer, LugarSerializer, MuralSerializer, JogoSerializer
from rest_framework import permissions

# Create your views here.

class FilmeView(ListAPIView):
    queryset = Filme.objects.order_by('id')
    serializer_class = FilmeSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

class LugarView(ListAPIView):
    queryset = Lugar.objects.order_by('id')
    serializer_class = LugarSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

class MuralView(ListAPIView):
    queryset = Mural.objects.order_by('id')
    serializer_class = MuralSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

class JogoView(ListAPIView):
    queryset = Jogo.objects.order_by('id')
    serializer_class = JogoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

