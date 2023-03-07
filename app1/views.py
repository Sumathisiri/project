from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>hi!!!!</h1>')

def second(request):
    return HttpResponse('<h1><marquee>Siri....</marquee></h1>')

