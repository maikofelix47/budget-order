from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from orders.models import OrderDetails, Order

# Create your models here.
class Dispatch(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])
    date_dispatched = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id},{self.date_dispatched},{self.order}"
