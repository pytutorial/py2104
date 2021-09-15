from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

@api_view(['GET'])
def search_product(request):
    keyword = request.GET.get('keyword', '')
    product_list = Product.objects.filter(name__icontains=keyword)
    data = ProductSerializer(product_list, many=True).data
    return Response(data)