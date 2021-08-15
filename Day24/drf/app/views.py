from rest_framework.response import Response
from rest_framework.decorators import api_view

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