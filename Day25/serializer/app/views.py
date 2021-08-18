from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from .models import *

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'#['phone', 'name']

    def validate_phone(self, phone):
        if not phone:       # blank
            return phone
        
        if not phone.isdigit():
            raise ValidationError('Số điện thoại chỉ được chứa chữ số')
        
        if len(phone) != 10 and len(phone) != 11:
            raise ValidationError('Số điện thoại phải chỉ được phép có 10/11 chữ số')

        return phone  # do not forget 'return' !!

@api_view(['GET'])
def get_customer_by_phone(request, phone):
    customer = Customer.objects.get(phone=phone)
    data = CustomerSerializer(customer).data
    # data = {'id': customer.id, 'name': customer.name, 'phone': customer.phone, ...}
    return Response(data)

@api_view(['GET'])
def search_customer(request):
    data = request.GET
    keyword = data.get('keyword', '')
    customer_list = Customer.objects.filter(name__icontains=keyword)
    data = CustomerSerializer(customer_list, many=True).data
    return Response(data)
    
@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def update_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    serializer = CustomerSerializer(
        data=request.data,
        instance=customer
    )
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data)

#============= Product====================
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 127.0.0.1:8000/api/get-product-by-code/IPX
@api_view(['GET'])
def get_product_by_code(request, code):
    product = Product.objects.get(code=code)
    data = ProductSerializer(product).data
    return Response(data)