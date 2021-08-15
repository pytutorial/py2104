from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.db.models import Q

# 127.0.0.1:8000/api/hello
@api_view(['GET'])
def hello(request):
    data = request.GET  # ?name=Nguyen+Van+A --> {'name': 'Nguyen Van A'}
    name = data.get('name', '')
    return Response({'message': f'Hello {name}'})

# 127.0.0.1:8000/api/hello-post
@api_view(['POST'])
def hello_post(request):
    data = request.data # Both form data + Json content type
    name = data.get('name', '')
    return Response({'message': f'Hello {name}'})

@api_view(['POST'])
def create_customer(request):
    data = request.data # {'name': '...', 'phone': '...', 'address': '...'}
    name = data.get('name', '')
    phone = data.get('phone', '')
    address = data.get('address', '')
    # Validate
    if name.strip() == '':
        return Response({'error': 'Họ tên không được thiếu'},status=400)
    
    if phone.strip() == '':
        return Response({'error': 'Số điện thoại không được thiếu'},status=400)
    
    if Customer.objects.filter(phone=phone).exists():
        return Response({'error': 'Số điện thoại đã tồn tại'}, status=400)

    Customer.objects.create(
        name=name,
        phone=phone,
        address=address
    )
    return Response({'success': True})

def serialize_customer(customer):
    return {
        'id': customer.id,
        'name': customer.name,
        'phone': customer.phone,
        'address': customer.address
    }

#127.0.0.1:8000/api/search-customer?keyword=A
@api_view(['GET'])
def search_customer(request):
    data = request.GET
    keyword = data.get('keyword', '')
    customer_list = Customer.objects.filter(name__icontains=keyword)
    #customer_list = Customer.objects.filter(
    #    Q(name__icontains=keyword)|Q(phone__icontains=keyword)
    #)
    data = []
    for customer in customer_list:
        data.append(serialize_customer(customer))
    # data = [serialize_customer(customer) for customer_list]
    return Response(data)

#127.0.0.1:8000/api/update-customer/1
@api_view(['PUT'])
def update_customer(request, pk):
    data = request.data
    name = data.get('name', '')
    phone = data.get('phone', '')
    address = data.get('address', '')
    #TODO: validate
    customer = Customer.objects.get(pk=pk)
    customer.name = name
    customer.phone = phone
    customer.address = address
    customer.save()  # commit to DB
    return Response({'success': True})

#127.0.0.1:8000/api/delete-customer/1
@api_view(['DELETE'])
def delete_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    return Response({'success': True})