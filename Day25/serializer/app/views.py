from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer
from .models import *

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

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