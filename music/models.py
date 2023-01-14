from django.db import models

# A model to track amount of links clicked on each link button

# A model to create 'artists-profiles' for each artist


class artist(models.Model):
    artist_name = models.CharField(max_length=254)
    artist_image = models.ImageField(null=True, blank=True)
    artist_bio = models.TextField()
    artist_link_bandcamp = models.URLField(max_length=1024, null=True, blank=True)
    artist_link_spotify = models.URLField(max_length=1024, null=True, blank=True)
    artist_link_soundcloud = models.URLField(max_length=1024, null=True, blank=True)

    bandcamp_counter = models.IntegerField(default=0)
    spotify_counter = models.IntegerField(default=0)
    soundcloud_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.artist_name



