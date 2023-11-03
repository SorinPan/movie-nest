import os
from django.shortcuts import render
import requests

API_KEY = os.environ.get("API_KEY")

def top_rated_movies(request):
    """
    Call on the TMDB API to provide some trending movies
    """
    endpoint = "https://api.themoviedb.org/3/movie/top_rated"

    params = {
        "api_key": API_KEY,
        "language": "en-US",  
        "page": 1  
    }

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        top_rated_movies = response.json().get("results", [])
        return render(request, 'movies/top_rated.html', {'top_rated_movies': top_rated_movies})
    else:
        error_message = f"API request failed with status code {response.status_code}"
        return render(request, 'movies/error.html', {'error_message': error_message})
