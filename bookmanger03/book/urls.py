from django.urls import path

from book.views import index, shop, cook
# from django.urls import converters
import book.converters

urlpatterns = [
    path('index/', index),
    path('<int:city_id>/<phone:shop_id>/', shop),
    path('cook/', cook),
]