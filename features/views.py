from .models import Feature
from .serializers import FeatureSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

# List features
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def all_features(request):
    if request.method == 'GET':
        feature = Feature.objects.all()
        feature_serializer = FeatureSerializer(feature, many=True)
        return JsonResponse(feature_serializer.data, safe=False)
    

    elif request.method == 'POST':
        feature_serializer = FeatureSerializer(data=request.data)
        if feature_serializer.is_valid():
            feature_serializer.save()
            return JsonResponse(feature_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Specific type of features
@api_view(['GET'])
def type_features(request, feature_type):
    feature = Feature.objects.filter(type=feature_type)
    
    if request.method == 'GET': 
        feature_serializer = FeatureSerializer(feature, many=True)
        return JsonResponse(feature_serializer.data, safe=False)
    
# Detail feature
@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes((IsAuthenticatedOrReadOnly,))
def feature_detail(request, feature_id):
    try:
        feature = Feature.objects.get(pk=feature_id)
    except Feature.DoesNotExist:
        return JsonResponse({'message' : 'A feature nao existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        feature_serializer = FeatureSerializer(feature)
        return JsonResponse(feature_serializer.data)
    
    if request.method == 'PUT':
        feature_serializer = FeatureSerializer(data=request.data)
        if feature_serializer.is_valid():
            feature_serializer.save()
            return JsonResponse(feature_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        feature.delete()
        return JsonResponse({'message' : 'Feature deletada com sucesso!'}, status=status.HTTP_204_NO_CONTENT)