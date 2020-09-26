import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def name(request):
    data = request.GET
    username = data.get('username')
    print(username)

    return HttpResponse(username)


def look(request, name, mobile):
    print(name, mobile)
    print(request.GET.keys())
    # request.GET.
    return HttpResponse(name, mobile)


def eat(request):
    data = request.POST
    print(f'data:{data}')

    return HttpResponse('post')


def register(request):
    data = request.body
    print(f'data:{data}, type:{type(data)}')
    data_str = data.decode()
    print(f'data:{data_str}, type:{type(data_str)}')
    data_dict = json.loads(data_str)
    print(f'data:{data_dict}, type:{type(data_dict)}')
    print(request.path)
    print(request.META.get('HTTP_NAME'))

    return HttpResponse('json')


def set_cookie(request):
    username = request.GET.get('username', max_age=60*60)
    password = request.GET.get('password')

    response = HttpResponse('set_cookie')
    response.set_cookie('username', username)
    response.set_cookie('password', password)

    return response


def get_cookie(request):
    name = request.COOKIES.get('username')
    pw = request.COOKIES.get('password')
    # cookie = request.COOKIES
    return HttpResponse(f'username:{name}, password:{pw}')


class SetSession(View):
    def post(self, request):
        name = request.POST.get('name')
        pw = request.POST.get('password')
        print(name, pw)
        request.session['name'] = name
        request.session['password'] = pw

        return HttpResponse('set_session')

    def get(self, request):
        name = request.GET.get('name')
        pw = request.GET.get('password')
        print(name, pw)
        request.session['name'] = name
        request.session['password'] = pw

        return HttpResponse('set_session')


def get_session(request):
    name = request.session.get('name')
    pw = request.session.get('password')
    # print(request.session)
    request.session.flush()
    return HttpResponse(f'name:{name}, pw:{pw}')

