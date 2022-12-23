from rest_framework import serializers
from .models import Reclamacao, ChatReclamacao

class ReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacao
        fields = '__all__'

class ChatReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatReclamacao
        fields = '__all__'