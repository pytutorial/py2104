from django.db import models

# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name