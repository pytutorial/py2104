from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.serializers import ModelSerializer, CharField, DateTimeField
from .models import *

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    customerName = CharField(read_only=True, source="customer.name")
    productName = CharField(read_only=True, source="product.name")
    orderDate = DateTimeField(format='%d/%m/%Y %H:%M:%S')

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

@api_view(['GET'])
def list_order(request):
    order_list = Order.objects.all()
    data = OrderSerializer(order_list, many=True).data
    return Response(data)