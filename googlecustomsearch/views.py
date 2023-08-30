import os
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse

@api_view(['GET'])
def search_photo(request, search_term):
    search_key = os.getenv('GOOGLE_CUSTOM_SEARCH_KEY')
    search_cx = os.getenv('GOOGLE_CUSTOM_SEARCH_CX')
    
    google_url = f"https://www.googleapis.com/customsearch/v1?key={search_key}&cx={search_cx}&q={search_term}&searchType=image"
    if request.method == 'GET':
        try:
            response = requests.get(google_url)

            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data, safe=False)
            else:
                    return JsonResponse({'error': 'Failed to fetch data from google API'}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Error accessing google API: ' + str(e)}, status=500)