from django.views import generic
from .models import artist, latestMusic


class artistList(generic.ListView):
    model = artist
    queryset = artist.objects.order_by('created_on')
    template_name = 'music.html'
    paginate_by = 6


class latestMusicList(generic.ListView):
    model = latestMusic
    queryset = latestMusic.objects.order_by('created_on')
    template_name = 'latest_music.html'
    paginate_by = 6
