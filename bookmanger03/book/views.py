import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


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
    try:
        print(f'body:{body}')
        body_str = body.decode()
        print(f'body_str:{body_str}')

        body_eval = eval(body_str)
        print(f'body_eval:{body_eval}')

        body_dict = json.loads(body_str)
        print(f' body_dict:{body_dict}')

        print(request.META['HTTP_NAME'])

    except Exception as e:
        print(e)
    info = {
        "name": "张三",
        "adress": "shunyi"

    }

    response = JsonResponse(info, content_type='text/html; charset=utf-8')
    # response['Content-Type'] = 'text/html; charset=utf-8'

    return response


def respon(request):

    return redirect('/index')


def cookie(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    print(username, password)
    name = request.COOKIES.get('username')
    pw = request.COOKIES.get('password')
    print('{}, {}'.format(name, pw))

    ck = request.COOKIES
    print(f'ck{ck}, type:{type(ck)}')
    flag = True
    if username and password:
        if name != username or pw != password:
            flag = False
    if name and pw and flag:

        jresponse = JsonResponse(ck)
        # jresponse.delete_cookie('username')

        return jresponse
    else:
        response = HttpResponse('set_cookie')
        response.set_cookie('username', username, max_age=60*2)
        response.set_cookie('password', password)

        return response


def session(request):
    session_dj = request.session.get('username')
    name = request.GET.get('username')
    if not session_dj or session_dj != name and name:
        request.session['username'] = name
        return HttpResponse('set-session')

    return HttpResponse(session_dj)
