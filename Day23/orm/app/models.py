from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    phone = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    qty = models.IntegerField()
    price_unit = models.IntegerField()
    total = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)