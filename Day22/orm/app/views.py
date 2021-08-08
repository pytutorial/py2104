from django.shortcuts import HttpResponse
from .models import *
import json

# Create your views here.
def get_product_by_code(request, code):
    product = Product.objects.get(code=code)
    data = {
        'id': product.id,
        'name': product.name,
        'code': product.code,
        'description': product.description,
        'price': product.price
    }
    return HttpResponse(json.dumps(data))

def search_product(request):
    input_data = request.GET
    keyword = input_data.get('keyword', '')
    product_list = Product.objects.filter(
        name__icontains=keyword)
    result = [product.name for product in product_list]
    return HttpResponse(','.join(result))

def get_customer_by_phone(request, phone):
    customer = Customer.objects.get(phone=phone)
    return HttpResponse(customer.name)

def search_customer(request):
    input_data = request.GET
    keyword = input_data.get('keyword', '')
    print('keyword=', keyword)
    customer_list = Customer.objects.filter(name__icontains=keyword)
    print('customer_list=', customer_list)
    result = ','.join([customer.name for customer in customer_list])
    return HttpResponse(result)