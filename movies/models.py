from django.db import models

class Movie(models.Model):
    """
    Model for movie
    """
    movie_id = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    certification = models.CharField(max_length=10)
    runtime = models.IntegerField()
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.title
