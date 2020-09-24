import json

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


def fromdate(request):
    data = request.POST
    # print(data)
    print(data['name'])
    print(data.get('password'))

    return HttpResponse('from')


def res(request):
    body = request.body
    print(f'body:{body}')
    body_str = body.decode()
    print(f'body_str:{body_str}')

    body_eval = eval(body_str)
    print(f'body_eval:{body_eval}')

    body_dict = json.loads(body_str)
    print(f' body_dict:{body_dict}')

    print(request.META['HTTP_NAME'])

    return HttpResponse('res')
