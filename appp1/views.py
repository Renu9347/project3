from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def appp1(request):
    return HttpResponse('<marquee><h1>This is my first application</marquee></h1>')
   
