#app1/views.py
from django.shortcuts import HttpResponse

# Create your views here.
# 127.0.0.1:8000/app-1/page-1
def page1(request):
    return HttpResponse('Page-1')
