from django.shortcuts import HttpResponse
from .models import *
import json

# Create your views here.

def serialize_product(product):
    return {
        'id': product.id,
        'name': product.name,
        'code': product.code,
        'description': product.description,
        'price': product.price
    }

def get_product_by_code(request, code):
    product = Product.objects.get(code=code)
    data = serialize_product(product)
    return HttpResponse(json.dumps(data))

def search_product(request):
    input_data = request.GET
    keyword = input_data.get('keyword', '')
    product_list = Product.objects.filter(
        name__icontains=keyword)
    result = [serialize_product(product) for product in product_list]
    return HttpResponse(json.dumps(result))

def search_product_by_price(request):
    input_data = request.GET
    print('input_data=', input_data)
    min_price = int(input_data['min_price']) * 1000000
    max_price = int(input_data['max_price']) * 1000000
    print('min_price=', min_price, ', max_price=', max_price)
    product_list = Product.objects.filter(
        price__gte=min_price,   # price >= min_price
        price__lte=max_price    # price <= max_price
    )
    result = [serialize_product(product) for product in product_list]
    return HttpResponse(json.dumps(result))

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