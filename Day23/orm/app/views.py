from django.shortcuts import HttpResponse
from .models import *
import json
from django.db.models import Q

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
    #print('input_data=', input_data)
    product_list = Product.objects.all()
    if 'min_price' in input_data:
        min_price = int(input_data['min_price']) * 1000000
        product_list = product_list.filter(price__gte=min_price)
    
    if 'max_price' in input_data:
        max_price = int(input_data['max_price']) * 1000000
        product_list = product_list.filter(price__lte=max_price)
    
    #print('min_price=', min_price, ', max_price=', max_price)

    #product_list = Product.objects.filter(
    #    price__gte=min_price,   # price >= min_price
    #    price__lte=max_price    # price <= max_price
    #)
    result = [serialize_product(product) for product in product_list]
    return HttpResponse(json.dumps(result))

def serialize_customer(customer):
    return {
        'id': customer.id,
        'name': customer.name,
        'phone': customer.phone,
        'address': customer.address
    }

def get_customer_by_phone(request, phone):
    customer = Customer.objects.get(phone=phone)
    data = serialize_customer(customer)
    return HttpResponse(json.dumps(data))

def search_customer(request):
    input_data = request.GET
    keyword = input_data.get('keyword', '')
    print('keyword=', keyword)

    customer_list = Customer.objects.filter(
        Q(name__icontains=keyword)|Q(phone__icontains=keyword)
    )

    print('customer_list=', customer_list)
    result = json.dumps([serialize_customer(customer) for customer in customer_list])
    return HttpResponse(result)

def serialize_order(order):
    return {
        'id': order.id,
        'customer_name': order.customer.name,
        'product_name': order.product.name,
        'qty': order.qty,
        'price_unit': order.price_unit,
        'total': order.total,
        'created_date': str(order.created_date)
    }

#127.0.0.1:8000/search-order-by-product/IPX
def search_order_by_product(request, product_code):
    order_list = Order.objects.filter(product__code=product_code)
    result = json.dumps([serialize_order(order) for order in order_list])
    return HttpResponse(result)

#127.0.0.1:8000/search-order-by-customer/0123456789
def search_order_by_customer(request, customer_phone):
    order_list = Order.objects.filter(customer__phone=customer_phone)
    result = json.dumps([serialize_order(order) for order in order_list])
    return HttpResponse(result)