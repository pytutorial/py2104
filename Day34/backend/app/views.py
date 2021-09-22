from django.shortcuts import render
from .models import Customer

# Create your views here.
def index(request):
    return render(request, 'index.html')

#127.0.0.1:8000/list-customer
def list_customer(request):
    customer_list = Customer.objects.all()
    context = {'customer_list': customer_list}
    return render(request, 'list_customer.html', context)