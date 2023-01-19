from django.db import models
from .widgets import CustomClearableFileInput

# A model to track amount of links clicked on each link button

# A model to create 'artists-profiles' for each artist


class artist(models.Model):
    artist_name = models.CharField(max_length=254)
    artist_image = models.ImageField(null=True, blank=True)
    artist_image_url = models.URLField(max_length=1024, null=True, blank=True)
    artist_bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.artist_name

class latestMusic(models.Model):
    artist_name = models.CharField(max_length=254)
    track_image = models.ImageField(null=True, blank=True)
    track_image_url = models.URLField(max_length=1024, null=True, blank=True)
    track_bio = models.TextField()
    track_link = models.URLField(max_length=1024, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artist_name


