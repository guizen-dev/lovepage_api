from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http.response import JsonResponse
from rest_framework import status
from .models import Reclamacao, ChatReclamacao
from .serializers import ReclamacaoSerializer, ChatReclamacaoSerializer


# NOTES
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def notes_list(request):
    if request.method == 'GET':
        notes = Reclamacao.objects.all()
        notes_serializer = ReclamacaoSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False, status=status.HTTP_200_OK)
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def notes_detail(request, note_id):
    try:
        note = Reclamacao.objects.get(pk=note_id)
    except Reclamacao.DoesNotExist:
        return JsonResponse({'message' : 'A reclamacao nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        note_serializer = ReclamacaoSerializer(note)
        return JsonResponse(note_serializer.data)

# RECLAMAÇÃO
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def chat_note_list(request):
    if request.method == 'GET':
        chat_note = ChatReclamacao.objects.all()
        chat_note = ChatReclamacaoSerializer(chat_note, many=True)
        return JsonResponse(chat_note.data, safe=False)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def chat_notes_detail(request, chat_id):
    try:
        chat_note = ChatReclamacao.objects.get(pk=chat_id)
    except ChatReclamacao.DoesNotExist:
        return JsonResponse({'message' : 'O chat da reclamacao nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        note_serializer = ChatReclamacaoSerializer(chat_note)
        return JsonResponse(note_serializer.data)
                       
@api_view(['GET', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def messages_note(request, note_id):
    try:
        messages = ChatReclamacao.objects.filter(reclamacao=note_id)
    except ChatReclamacao.DoesNotExist:
        return JsonResponse({'message' : 'As mensagens não existem ou o id da reclamação está errado'}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        messages_serializer = ChatReclamacaoSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    