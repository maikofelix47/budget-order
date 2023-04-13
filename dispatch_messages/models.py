from django.db import models

# Create your models here.
from orders.models import Order
from riders.models import Rider

# Create your models here.
class DispatchMessage(models.Model):
    message = models.TextField()
    recepient = models.ForeignKey(Rider,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id},{self.recepient}"

