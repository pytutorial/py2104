from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name