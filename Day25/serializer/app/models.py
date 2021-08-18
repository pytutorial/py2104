from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Customer(models.Model):
    phone = CharField(max_length=20, unique=True)
    name = CharField(max_length=100)
    address = CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name