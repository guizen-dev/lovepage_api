from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse

@api_view(['GET', 'POST'])
def usuario_list(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        tutorials_serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

            
    
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST', 'DELETE'])
def usuario_detail(request, usuario_id):
    try:
        usuario = Usuario.objects.get(pk=usuario_id)
    except Usuario.DoesNotExist:
        return JsonResponse({'message' : 'O usuario nao existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        usuario_serializer = UsuarioSerializer(usuario)
        return JsonResponse(usuario_serializer.data)
    
    if request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data)
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'message' : 'Usuario foi deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
        