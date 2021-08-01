from django.shortcuts import HttpResponse

#127.0.0.1:8000 
def index(request):
    return HttpResponse('Hello')

#127.0.0.1:8000/page-2
def page2(request):
    return HttpResponse('Page-2')