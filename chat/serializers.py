from rest_framework import serializers
from .models import Reclamacao, ChatReclamacao

class ReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacao
        fields = ['id', 'title', 'state', 'user']

class ChatReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatReclamacao
        fields = ['id', 'reclamacao', 'user', 'message']