from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact.as_view(), name='contact'),
    path('terms', views.terms.as_view(), name='terms'),
]
