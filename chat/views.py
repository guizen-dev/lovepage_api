from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from rest_framework import status
from .models import Reclamacao, ChatReclamacao
from .serializers import ReclamacaoSerializer, ChatReclamacaoSerializer

# Create your views here.      

# NOTES
@api_view(['GET', 'POST'])
def notes_list(request):
    if request.method == 'GET':
        notes = Reclamacao.objects.all()
        notes_serializer = ReclamacaoSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        notes_data = JSONParser().parse(request)
        notes_serializer = ReclamacaoSerializer(data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse(notes_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(notes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def notes_detail(request, note_id):
    try:
        note = Reclamacao.objects.get(pk=note_id)
    except Reclamacao.DoesNotExist:
        return JsonResponse({'message' : 'A reclamacao nao existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        note_serializer = ReclamacaoSerializer(note)
        return JsonResponse(note_serializer.data)
    
    if request.method == 'PUT':
        note_data = JSONParser().parse(request)
        note_serializer = ReclamacaoSerializer(note, data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data)
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        note.delete()
        return JsonResponse({'message' : 'A reclamacao foi deletada com sucesso'}, status=status.HTTP_204_NO_CONTENT)
    
    
# RECLAMAÇÃO
@api_view(['GET', 'POST'])
def chat_note_list(request):
    if request.method == 'GET':
        chat_note = ChatReclamacao.objects.all()
        chat_note = ChatReclamacaoSerializer(chat_note, many=True)
        return JsonResponse(chat_note.data, safe=False)

    elif request.method == 'POST':
        notes_data = JSONParser().parse(request)
        chat_note = ChatReclamacaoSerializer(data=notes_data)
        if chat_note.is_valid():
            chat_note.save()
            return JsonResponse(chat_note.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(chat_note.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def chat_notes_detail(request, chat_id):
    try:
        chat_note = ChatReclamacao.objects.get(pk=chat_id)
    except ChatReclamacao.DoesNotExist:
        return JsonResponse({'message' : 'O chat da reclamacao nao existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        note_serializer = ChatReclamacaoSerializer(chat_note)
        return JsonResponse(note_serializer.data)
    
    if request.method == 'PUT':
        note_data = JSONParser().parse(request)
        note_serializer = ChatReclamacaoSerializer(chat_note, data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse(note_serializer.data)
        return JsonResponse(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        chat_note.delete()
        return JsonResponse({'message' : 'O chat da reclamacao foi deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'DELETE'])
def messages_note(request, note_id):
    try:
        messages = ChatReclamacao.objects.filter(reclamacao=note_id)
    except ChatReclamacao.DoesNotExist:
        return JsonResponse({'message' : 'As mensagens não existem ou o id da reclamação está errado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        messages_serializer = ChatReclamacaoSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    
    if request.method == 'DELETE':
        messages.delete()
        return JsonResponse({'message' : 'As mensagens foram excluídas com sucesso'}, status=status.HTTP_204_NO_CONTENT)