from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

class artistAdmin(SummernoteModelAdmin):
    list_display = ('artist_name', 'artist_image', 'artist_link_bandcamp', 'artist_link_spotify', 'artist_link_soundcloud')
    summernote_fields = ('artist_bio')

class latestMusicAdmin(SummernoteModelAdmin):
    list_display = ('artist_name', 'track_image', 'track_link_bandcamp', 'track_link_spotify', 'track_link_soundcloud')
    summernote_fields = ('track_bio')

admin.site.register(models.artist, artistAdmin)
admin.site.register(models.latestMusic, latestMusicAdmin)



