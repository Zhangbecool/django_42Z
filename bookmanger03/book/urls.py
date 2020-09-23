from django.urls import path

from book.views import index, shop, cook

urlpatterns = [
    path('index/', index),
    path('<city_id>/<shop_id>/', shop),
    path('cook/', cook),
]