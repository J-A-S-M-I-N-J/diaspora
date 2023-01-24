from django.shortcuts import render
from django.views import View


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
