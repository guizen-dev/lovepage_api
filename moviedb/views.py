from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
import os

# Create your views here.

@api_view(['GET'])
def get_movies(request, search_term):
    apikey = str(os.getenv('MOVIEDB_API_KEY'))
    moviedb_url = 'https://api.themoviedb.org/3/search/movie?api_key='+apikey+'&query='+search_term
    
    if request.method == 'GET':
        try:
            response = requests.get(moviedb_url)

            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data)
            else:
                return JsonResponse({'error': 'Failed to fetch data from moviedb API'}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Error accessing moviedb API: ' + str(e)}, status=500)