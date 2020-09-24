from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def name(request, name):
    print(name)

    return HttpResponse(name)


def look(request, name, height):
    print(name, height)
    print(request.GET.keys())
    # request.GET.
    return HttpResponse(name, height)
