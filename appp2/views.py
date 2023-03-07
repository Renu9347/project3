from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def appp2(request):
    return HttpResponse('<marquee><h1>This is my second application</marquee></h1>')
