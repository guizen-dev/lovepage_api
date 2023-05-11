from .models import Feature
from .serializers import FeatureSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.http.response import JsonResponse

# Create your views here.

# List features
@api_view(['GET', 'POST'])
def all_features(request):
    if request.method == 'GET':
        feature = Feature.objects.all()
        feature_serializer = FeatureSerializer(feature, many=True)
        return JsonResponse(feature_serializer.data, safe=False)

    elif request.method == 'POST':
        feature_data = JSONParser().parse(request)
        feature_serializer = FeatureSerializer(data=feature_data)
        if feature_serializer.is_valid():
            feature_serializer.save()
            return JsonResponse(feature_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Specif type of features
@api_view(['GET'])
def type_features(request, feature_type):
    feature = Feature.objects.filter(type=feature_type)
    
    if request.method == 'GET': 
        feature_serializer = FeatureSerializer(feature, many=True)
        return JsonResponse(feature_serializer.data, safe=False)
    
# Detail feature
@api_view(['GET', 'PUT', 'DELETE'])
def feature_detail(request, feature_id):
    try:
        feature = Feature.objects.get(pk=feature_id)
    except Feature.DoesNotExist:
        return JsonResponse({'message' : 'A feature nao existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        feature_serializer = FeatureSerializer(feature)
        return JsonResponse(feature_serializer.data)
    
    if request.method == 'PUT':
        feature_data = JSONParser().parse(request)
        feature_serializer = FeatureSerializer(feature, data=feature_data)
        if feature_serializer.is_valid():
            feature_serializer.save()
            return JsonResponse(feature_serializer.data)
        return JsonResponse(feature_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        feature.delete()
        return JsonResponse({'message' : 'Feature deletada com sucesso!'}, status=status.HTTP_204_NO_CONTENT)