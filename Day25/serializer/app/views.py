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

    