from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

class artistAdmin(SummernoteModelAdmin):
    list_display = ('artist_name', 'artist_image', 'created_on')
    summernote_fields = ('artist_bio')

class latestMusicAdmin(SummernoteModelAdmin):
    list_display = ('artist_name', 'track_image', 'created_on', 'track_link')
    summernote_fields = ('track_bio')

admin.site.register(models.artist, artistAdmin)
admin.site.register(models.latestMusic, latestMusicAdmin)



