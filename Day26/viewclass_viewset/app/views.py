from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.serializers import ModelSerializer, CharField, DateTimeField, SerializerMethodField
from .models import *

from rest_framework.views import APIView

class HelloView(APIView):
    def get(self, request):
        data = request.GET
        name = data.get('name', '')
        return Response({'message': f'Hello {name}'})

    def post(self, request):
        data = request.data
        name = data.get('name', '')
        return Response({'message': f'Hello {name}'})

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    customerName = CharField(read_only=True, source="customer.name")
    productName = CharField(read_only=True, source="product.name")
    orderDate = DateTimeField(format='%d/%m/%Y %H:%M:%S')
    total = SerializerMethodField()

    def get_total(self, obj:Order):
        return obj.qty * obj.priceUnit

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

@api_view(['GET'])
def list_order(request):
    order_list = Order.objects.all()
    data = OrderSerializer(order_list, many=True).data
    return Response(data)

