from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('index')


def shop(request, city_id, shop_id):
    print(f'city:{city_id}, shop:{shop_id}')

    return HttpResponse(f'city:{city_id}, shop:{shop_id}')


def cook(request):
    name = request.GET.get('kw')
    l = request.GET.getlist('order')
    print(l)
    print(name)

    return HttpResponse(f'{name}, {l}')
