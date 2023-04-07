from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from products.models import Product

# Create your models here.

class Order(models.Model):
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id}"


class OrderDetails(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'OrderDetails'


