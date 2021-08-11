"""orm URL Configuration

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
    path('get-customer-by-phone/<phone>', get_customer_by_phone),
    path('search-customer', search_customer),
    path('get-product-by-code/<code>', get_product_by_code),
    path('search-product', search_product),
    path('search-product-by-price', search_product_by_price),
    path('search-order-by-product/<product_code>', search_order_by_product),
    path('search-order-by-customer/<customer_phone>', search_order_by_customer),
    path('admin/', admin.site.urls),
]
