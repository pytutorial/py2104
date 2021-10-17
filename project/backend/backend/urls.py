"""backend URL Configuration

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
from app.views_api import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token', jwt_views.TokenObtainPairView.as_view()),
    path('api/order-product/<pk>', order_product),
    path('api/get-product-list', get_product_list),
    path('api/get-customer-list', get_customer_list),
    path('', index),
    path('list-customer', list_customer),
    path('api/create-customer', create_customer),
    path('view-product/<pk>', view_product),
    path('admin/', admin.site.urls),
]

routers = DefaultRouter()
routers.register('api/category', CategoryViewSet)
urlpatterns += routers.urls

routers = DefaultRouter()
routers.register('api/product', ProductViewSet)
urlpatterns += routers.urls
