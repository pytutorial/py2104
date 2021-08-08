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