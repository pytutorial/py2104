#app1/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('page-1', page1),
]