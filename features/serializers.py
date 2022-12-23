from rest_framework import serializers
from .models import Filme, Lugar, Mural, Jogo

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class MuralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mural
        fields = '__all__'

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'