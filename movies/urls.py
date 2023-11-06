from django.urls import path
from . import views


urlpatterns = [
    path('top-rated/', views.movie_categories, {'category': 'top_rated'}, name='top_rated_movies'),
    path('trending/', views.movie_categories, {'category': 'trending'}, name='trending_movies'),
    path("movie_details/<int:movie_id>", views.movie_details, name="movie_details"),
]