from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hydrabad(request):
    return HttpResponse('<h1>sunrises hydrabad</h1>')