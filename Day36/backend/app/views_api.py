from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer, CharField

from rest_framework.viewsets import ModelViewSet
from .models import Customer, Product
from .models import Order

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer_phone', 'customer_name', 'customer_address', 'qty']

@api_view(['POST'])
def order_product(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = OrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    order = Order()
    order.customer_phone = request.data['customer_phone']
    order.customer_name = request.data['customer_name']
    order.customer_address = request.data['customer_address']
    order.qty = request.data['qty']
    order.product = product
    order.price_unit = product.price
    order.order_date = datetime.now()
    order.status = Order.Status.PENDING
    order.save()

    return Response({'success': True})

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    else:
        serializer.save()
        return Response({'success': True})

PAGE_SIZE = 2

@api_view(['GET'])
def get_customer_list(request):
    name = request.GET.get('name', '')
    customer_list = Customer.objects.filter(name__icontains=name)
    total = customer_list.count()
    page = int(request.GET.get('page') or 1)
    customer_list = customer_list[(page-1)*PAGE_SIZE:page*PAGE_SIZE]
    data = CustomerSerializer(customer_list, many=True).data
    return Response({'total': total, 'data': data})

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