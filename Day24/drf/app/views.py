from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *

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
def create_user(request):
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