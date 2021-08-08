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
    product_list = Product.objects.filter(name__icontains=keyword)
    result = [product.name for product in product_list]
    return HttpResponse(','.join(result))