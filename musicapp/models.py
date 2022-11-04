from django.db import models
from datetime import datetime
# Create your models here.

class Artiste (models.Model):
    first_name = models.CharField(max_length=400, default = "Enter First Name")
    last_name = models.CharField(max_length=400, default = "Enter Last Name")
    age = models.IntegerField(default = 1)

    def __str__(self):
        return self.first_name +  ' ' + self.last_name

class Song (models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=400, default = "Song Title")
    date_released = models.DateTimeField(default = datetime.now())
    likes = models.CharField(max_length=400, default = "DEFAULT VALUE")
    artiste_identity = models.CharField(max_length=400, default = "")

    def __str__(self):
        return self.title

class Lyric (models.Model):
    content = models.TextField(default = "Content")
    lyrics_title = models.CharField(max_length=200, default = "")
    Song = models.ForeignKey(Song, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.lyrics_title