from django.shortcuts import HttpResponse
from .models import *

# Create your views here.
def get_product_by_code(request, code):
    product = Product.objects.get(code=code)
    return HttpResponse(product.name)