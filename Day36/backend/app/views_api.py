from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer, CharField

from rest_framework.viewsets import ModelViewSet
from .models import Customer, Product

PAGE_SIZE = 2

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

@api_view(['GET'])
def get_customer_list(request):
    start = int(request.GET.get('start') or 0)
    count = int(request.GET.get('count') or PAGE_SIZE)
    name = request.GET.get('name', '')
    customer_list = Customer.objects.filter(name__icontains=name)
    total = customer_list.count()
    items = customer_list[start:start+count]
    data = CustomerSerializer(items, many=True).data
    return Response({'items': data, 'total': total})

@api_view(['GET'])
def get_product_list(request):
    name = request.GET.get('name', '')
    product_list = Product.objects.filter(name__icontains=name)
    data = ProductSerializer(product_list, many=True).data
    return Response(data)

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    category_name = CharField(read_only=True, source='category.name')

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()