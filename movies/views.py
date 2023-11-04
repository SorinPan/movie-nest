import os
from django.shortcuts import render
import requests

API_KEY = os.environ.get("API_KEY")

def movie_categories(request, category):
    """
    Request movie data from TMDB api based on category
    """
    category_mapping = {
        "top_rated": {
            "url": f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page",
            "template": "movies/top_rated.html",
        }
    }

    category_info = category_mapping.get(category)

    if category_info:
        url = category_info["url"]
        template_name = category_info["template"]
        response = requests.get(url)
        movie_info = response.json()

        context = {
            "movie_info": movie_info,
        }

        return render(request, template_name, context)
    else:
        return ("Something went wrong!")
