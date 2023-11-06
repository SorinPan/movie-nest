import os
from django.shortcuts import render
import requests

API_KEY = os.environ.get("API_KEY")

def movie_categories(request, category, page_number=1):
    """
    Request movie info from TMDB api based on category
    """
    category_mapping = {
        "top_rated": {
            "url": f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page={page_number}",
            "template": "movies/top_rated.html",
        },
        "trending": {
            "url": f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}",
            "template": "movies/trending.html",
        },
    }

    category_info = category_mapping.get(category)

    if category_info:
        url = category_info["url"]
        template_name = category_info["template"]
        response = requests.get(url)
        movie_info = response.json()
        page_number = int(page_number)
        prev_page = page_number - 1 if page_number > 1 else None
        next_page = page_number + 1 if movie_info["total_pages"] > page_number else None

        context = {
            "movie_info": movie_info,
            "page_number": page_number,
            "prev_page": prev_page,
            "next_page": next_page,
        }

        return render(request, template_name, context)
    else:
        return ("Something went wrong!")

def movie_details(request, movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        movie_info = response.json()

        
        if "original_title" in movie_info and "overview" in movie_info:
            backdrop = movie_info.get("backdrop_path", "")
            hero = f"https://image.tmdb.org/t/p/w1280/{backdrop}"

            context = {
                "movie_info": movie_info,
                "hero": hero,
            }

            return render(request, "movies/movie_details.html", context)
        else:
            return render(request, "error.html", {"message": "Invalid movie data received from the API."})

    except requests.exceptions.RequestException as e:
        # Handle request-related errors, such as connection issues or timeouts
        return render(request, "error.html", {"message": f"API request failed: {str(e)}"})
