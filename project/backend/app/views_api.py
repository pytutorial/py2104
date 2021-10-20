from datetime import datetime
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer, CharField, DateTimeField, IntegerField

from rest_framework.viewsets import ModelViewSet
from .models import Category, Customer, Product
from .models import Order

PAGE_SIZE = 5

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer_phone', 'customer_name', 'customer_address', 'qty', 
                    'price_unit', 'status', 'order_date', 'deliver_date', 'product_name']
    
    product_name = CharField(read_only=True, source='product.name')
    price_unit = IntegerField(read_only=True)
    order_date = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    deliver_date = DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    status = IntegerField(read_only=True)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def search_order(request):
    name = request.GET.get('name', '')
    order_list = Order.objects.filter(
        Q(customer_name__icontains=name) |
        Q(customer_phone__icontains=name)|
        Q(product__name__contains=name)
    )
    total = order_list.count()
    page = int(request.GET.get('page') or 1)
    order_list = order_list[(page-1)*PAGE_SIZE:page*PAGE_SIZE]
    data = OrderSerializer(order_list, many=True).data
    return Response({'total': total, 'data': data})

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def view_order(request, pk):
    order = Order.objects.get(pk=pk)
    data = OrderSerializer(order).data
    return Response(data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def confirm_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.DELIVERED
    order.deliver_date = datetime.now()
    order.save()
    return Response({'success': True})

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def cancel_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.CANCELED
    order.save()
    return Response({'success': True})

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

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()