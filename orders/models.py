from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from products.models import Product

# Create your models here.

class Order(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    date_created = models.DateTimeField(auto_now=True)


