# django_auto_mapping
An url auto mapping tool for django 2.0+
Example
for urls.py:
from .mapping import auto_mapping
import myapp.views

urlpatterns = [
    auto_mapping('test/', myapp.views),
]

While myapp/views.py:

from django.http import HttpResponse

def index(request):
    return HttpResponse('hello')

def add(request,a:int,b:int):
    return HttpResponse(a+b)


Now visit yourdomain/test/add/1/2 and it will be routed automatically to views.add method.
