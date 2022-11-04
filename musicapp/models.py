from django.db import models

# Create your models here.

class Artiste (models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()


class Song (models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)
    title = models.CharField(max_length=400)
    date_released = models.DateTimeField()
    likes = models.CharField(max_length=400)
    artiste_id = models.CharField(max_length=400)

class Lyric (models.Model):
    content = models.TextField()
    song_id = models.CharField(max_length=400)
    Song = models.ForeignKey(Song, on_delete=models.PROTECT)