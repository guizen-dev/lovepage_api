from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Reclamacao, ChatReclamacao
from .serializers import ReclamacaoSerializer, ChatReclamacaoSerializer

# Create your views here.

class ReclamacaoListView(ListAPIView):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

    def post(self, request):
        serializer = Reclamacao(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReclamacaoAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def delete_chat(request, reclamacao_id):
        reclamacao = Reclamacao.objects.get(pk=reclamacao_id)
        try:
            reclamacao.delete()
            return render(request, 'delete_sucessfully.html')
        except:
            return render(request, 'unsucessfully_delete.html')
        


class ChatReclamacaoListView(ListAPIView):
    queryset = ChatReclamacao.objects.order_by('id')
    serializer_class = ChatReclamacaoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

    def post(self, request):
        serializer = ChatReclamacao(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChatReclamacaoAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def delete_chat(request, chat_id):
        chatReclamacao = ChatReclamacao.objects.get(pk=chat_id)
        try:
            chatReclamacao.delete()
            return render(request, 'delete_sucessfully.html')
        except:
            return render(request, 'unsucessfully_delete.html')
        

