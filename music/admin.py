from django.contrib import admin

from . import models

class artistAdmin(admin.ModelAdmin):
    list_display = (
        'artist_name',
        'artist_image',
        'artist_bio',
        'artist_link_bandcamp',
        'artist_link_spotify',
        'artist_link_soundcloud',
    )

class latestMusicAdmin(admin.ModelAdmin):
    list_display = (
        'artist_name',
        'track_image',
        'track_bio',
        'track_link_bandcamp',
        'track_link_spotify',
        'track_link_soundcloud',
    )



admin.site.register(models.artist, artistAdmin)
admin.site.register(models.latestMusic, latestMusicAdmin)