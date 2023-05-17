from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from django.contrib.auth.models import AbstractBaseUser
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class RegisterView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request):       
        if request.method == 'POST':
            usuario_serializer = UsuarioSerializer(data=request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def delete(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(pk=usuario_id)
        except Usuario.DoesNotExist:
            return JsonResponse({'message' : 'O usuario nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'DELETE':
            usuario.delete()
            return JsonResponse({'message' : 'Usuario foi deletado com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def all_users(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        usuario_serializer = UsuarioSerializer(usuario, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)

class LoginView(APIView):
    def post(self, request):
        user = request.data['user']
        password = request.data['password']
        
        try:
            usuario = Usuario.objects.filter(user=user).first()
            if not usuario.check_password(password):
                return JsonResponse({'message' : 'Senha incorreta'}, status=status.HTTP_401_UNAUTHORIZED)
        
            return JsonResponse({'message' : 'User logado'}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'message' : 'Usuario nao achado'}, status=status.HTTP_404_NOT_FOUND)
        
        
        #if user is None:
        #    raise AuthenticationFailed('User not found!')
        
        