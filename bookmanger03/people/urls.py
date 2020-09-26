from django.urls import path, register_converter
from people.views import *
from book.converters import mobile

register_converter(mobile, 'phone')

urlpatterns = [
    path('name/', name),
    path('<name>/<phone:mobile>', look),
    path('eat/', eat),
    path('register/', register),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', SetSession.as_view()),
    path('get_session/', get_session),
]
