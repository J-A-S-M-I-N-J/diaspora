from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.about.as_view(), name='contact'),
]
