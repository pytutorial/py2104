from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer

from .models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

@api_view(['GET'])
def get_customer_list():
    customer_list = Customer.objects.all()
    data = CustomerSerializer(customer_list, many=True).data
    return Response(data)