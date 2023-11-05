from django.test import TestCase
from .models import Movie

class MovieModelTest(TestCase):
    def test_movie_creation(self):
        # Create a movie
        movie = Movie.objects.create(
            movie_id="1",
            title="Test Title",
            overview="This is a movie about tests",
            release_date="2023-11-05",
            certification="R",
            runtime=126,
            director="Mr Tester",
        )

        # Check if the stored movie matches the created one
        self.assertEqual(stored_movie.movie_ide, "1")
        self.assertEqual(stored_movie.title, "Test Title")
        self.assertEqual(stored_movie.overview, "This is a movie about tests")
        self.assertEqual(stored_movie.release_date, "2023-11-05")
        self.assertEqual(stored_movie.certification, "R")
        self.assertEqual(stored_movie.runtime, 126)
        self.assertEqual(stored_movie.director, "R")
