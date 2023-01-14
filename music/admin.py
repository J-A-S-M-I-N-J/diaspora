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


admin.site.register(models.artist, artistAdmin)