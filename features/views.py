from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Filme, Lugar, Mural, Jogo
from .serializers import FilmeSerializer, LugarSerializer, MuralSerializer, JogoSerializer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import permissions, status
from rest_framework.response import Response
import json_parser
import io

# Create your views here.

class FilmeView(ListAPIView):
    queryset = Filme.objects.order_by('id')
    serializer_class = FilmeSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

    def request(self, request):
        if (request.method == "POST"):
            serializer = Filme(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    
class FilmeAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def delete_filme(request, filme_id):
        filme = Filme.objects.get(pk=filme_id)
        try:
            filme.delete()
            return render(request, 'delete_sucessfully.html')
        except:
            return render(request, 'unsucessfully_delete.html')



class LugarView(ListAPIView):
    queryset = Lugar.objects.order_by('id')
    serializer_class = LugarSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

    def post(self, request):
        serializer = Lugar(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LugarAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def delete_lugar(request, lugar_id):
        lugar = Lugar.objects.get(pk=lugar_id)
        try:
            lugar.delete()
            return render(request, 'delete_sucessfully.html')
        except:
            return render(request, 'unsucessfully_delete.html')



class MuralView(ListAPIView):
    queryset = Mural.objects.order_by('id')
    serializer_class = MuralSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

    def post(self, request):
        serializer = Mural(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MuralAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def delete_mural(request, mural_id):
        mural = Mural.objects.get(pk=mural_id)
        try:
            mural.delete()
            return render(request, 'delete_sucessfully.html')
        except:
            return render(request, 'unsucessfully_delete.html')



class JogoView(ListAPIView):
    queryset = Jogo.objects.order_by('id')
    serializer_class = JogoSerializer
    permission_classes = (permissions.AllowAny, )
    filterset_fields = ['id',]

    def post(self, request):
        serializer = Jogo(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class JogoAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    @api_view(('GET',))
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def delete_jogo(request, jogo_id):
        jogo = Jogo.objects.get(pk=jogo_id)
        try:
            jogo.delete()
            return render(request, 'delete_sucessfully.html')
        except:
            return render(request, 'unsucessfully_delete.html')