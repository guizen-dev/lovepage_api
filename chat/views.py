from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from .models import Reclamacao, ChatReclamacao
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReclamacaoSerializer, ChatReclamacaoSerializer

# Create your views here.

class ReclamacaoListView(ListAPIView):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

class ReclamacaoUpdateView(UpdateAPIView):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

class ReclamacaoDeleteView(DestroyAPIView):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]


class ChatReclamacaoListView(ListAPIView):
    queryset = ChatReclamacao.objects.order_by('id')
    serializer_class = ChatReclamacaoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]
