import os
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse


@api_view(['GET'])
def game_detail(request, game_id):
    
    if request.method == 'GET':
        access_token = os.getenv('IGDB_ACCESS_TOKEN')
        client_id = os.getenv('IGDB_CLIENT_ID')
        igdb_url = 'https://api.igdb.com/v4/games'
        igdb_artwork_url = 'https://api.igdb.com/v4/artworks'
        
        try:
            headers = {
                'Client-ID': client_id,
                'Authorization': f'Bearer {access_token}',
            }

            requestData = f'fields *; where id = {game_id};'

            detail_response = requests.post(igdb_url, data=requestData, headers=headers)            

            if detail_response.status_code == 200:
                data = detail_response.json()
                
                artworks_value = data[0]['artworks'][0]
                requestData = f'fields *; where id = {artworks_value};'
                artwork_response = requests.post(igdb_artwork_url, data=requestData, headers=headers)
                
                if detail_response.status_code == 200:
                    artwork_data = artwork_response.json()
                    combined_data = {
                        "detail_data": data,
                        "artwork_data": artwork_data
                    }
                    
                    return JsonResponse(combined_data, safe=False)
                else:
                    return JsonResponse(data, safe=False)
            else:
                return JsonResponse({'error': 'Failed to fetch data from igdb API'}, status=detail_response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Error accessing igdb API: ' + str(e)}, status=500)
    

@api_view(['GET'])
def search_games(request, search_term):
    access_token = os.getenv('IGDB_ACCESS_TOKEN')
    client_id = os.getenv('IGDB_CLIENT_ID')
    igdb_url = 'https://api.igdb.com/v4/search'

    if request.method == 'GET':
        try:
            headers = {
                'Client-ID': client_id,
                'Authorization': f'Bearer {access_token}',
            }

            requestData = f'search "{search_term}"; fields *;'

            response = requests.post(igdb_url, data=requestData, headers=headers)

            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse({'error': 'Failed to fetch data from igdb API'}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Error accessing igdb API: ' + str(e)}, status=500)
        
@api_view(['GET'])
def popular_games(request):
    rawg_api_key = os.getenv('RAWG_API_KEY')
    rawg_url = f'https://api.rawg.io/api/games?key={rawg_api_key}'

    if request.method == 'GET':
        try:

            response = requests.get(rawg_url)

            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse({'error': 'Failed to fetch data from rawg API'}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': 'Error accessing rawg API: ' + str(e)}, status=500)
