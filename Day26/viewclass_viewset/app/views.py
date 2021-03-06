from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from rest_framework.serializers import ModelSerializer, CharField, DateTimeField, SerializerMethodField
from .models import *

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

#============================ Product ViewSet ====================================
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(methods=['get'], detail=False)
    def search(self, request):
        data = request.GET
        keyword = data.get('keyword', '')
        product_list = Product.objects.filter(name__icontains=keyword)
        data = ProductSerializer(product_list, many=True).data
        return Response(data)

    @action(methods=['get'], detail=True)
    def get_price(self, request, pk):
        product = Product.objects.get(pk=pk)
        return Response({'price': product.price})

# ======================== Customer ViewSet ====================================
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    @action(methods=['get'], detail=False)
    def search(self, request):
        data = request.GET
        keyword = data.get('keyword', '')
        customer_list = Customer.objects.filter(name__icontains=keyword)
        data = CustomerSerializer(customer_list, many=True).data
        return Response(data)

    @action(methods=['get'], detail=True)
    def get_order_history(self, request, pk):
        order_list = Order.objects.filter(customer__id=pk)
        data = OrderSerializer(order_list, many=True).data
        return Response(data)

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

