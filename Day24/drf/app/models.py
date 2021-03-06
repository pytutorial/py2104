from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    # python manage.py makemigrations
    # python manage.py migrate

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name