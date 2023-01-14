from django.urls import path
from . import views


urlpatterns = [
    path('', views.artistList.as_view(), name='music'),
    path('', views.latestMusicList.as_view(), name='latestMusic'),
]
