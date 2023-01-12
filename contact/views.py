from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect

# Create your views here.

class contact(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'contact.html',
        )

class terms(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'terms.html',
        )