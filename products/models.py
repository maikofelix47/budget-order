from django.db import models

from stores.models import Store

# Create your models here.

class QuantityType(models.Model):
    name = models.CharField(max_length=10)
    units = models.CharField(max_length=10)



class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity_type = models.ForeignKey(QuantityType,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    voided = models.BooleanField(default=False)
    voided_date = models.DateTimeField(auto_now=False)

    def __str__(self) -> str:
        return f"{self.name}"
