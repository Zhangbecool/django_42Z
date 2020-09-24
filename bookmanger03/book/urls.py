from django.urls import path, register_converter

from book.views import *
# from django.urls import converters
from book.converters import mobile

register_converter(mobile, 'phone')




urlpatterns = [
    path('index/', index),
    path('<int:city_id>/<phone:shop_id>/', shop),
    path('cook/', cook),
    path('from/', fromdate),
    path('res/', res),
    path('respon/', respon),
    path('cookie/', cookie),
    path('session/', session),
]