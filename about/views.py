from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect

# Create your views here.

class about(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'about.html',
        )