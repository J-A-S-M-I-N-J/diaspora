from django.shortcuts import render
from django.views import generic
from .models import artist


#def music(request):
    #"""A view to return the music page"""
   # return render(request, 'music.html')

class artistList(generic.ListView):
    model = artist
    queryset = artist.objects.order_by('artist_name')
    template_name = 'music.html'
    paginate_by = 6
