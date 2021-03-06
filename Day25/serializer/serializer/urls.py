"""serializer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('api/update-customer/<pk>', update_customer),
    path('api/create-customer', create_customer),
    path('api/search-customer', search_customer),
    path('api/get-customer-by-phone/<phone>', get_customer_by_phone),
    path('api/hello', hello),
    path('admin/', admin.site.urls),

    path('api/get-product-by-code/<code>', get_product_by_code),
    path('api/search-product', search_product),
    path('api/create-product', create_product),
    path('api/update-product/<pk>', update_product),
]
