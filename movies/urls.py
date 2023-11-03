from django.urls import path
from . import views


urlpatterns = [
    path('top-rated/', views.top_rated_movies, name='top_rated_movies'),
]