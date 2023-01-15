from django.urls import path
from . import views


urlpatterns = [
    path('', views.artistList.as_view(), name='music'),
    path('music/', views.latestMusicList.as_view(), name='latestmusic'),
]
