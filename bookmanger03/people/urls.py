from django.urls import path
from people.views import *

urlpatterns = [
    path('<name>', name),
    path('<name>/<height>', look),
]