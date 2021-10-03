from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name

class Order(models.Model):
    class Status:
        PENDING = 0
        DELIVERED = 1
        CANCELED = 2
        
    customer_phone = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price_unit = models.IntegerField()
    qty = models.IntegerField()
    order_date = models.DateTimeField()
    deliver_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField()
