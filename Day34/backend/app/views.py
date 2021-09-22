from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

#127.0.0.1:8000/list-customer
def list_customer(request):
    return render(request, 'list_customer.html')