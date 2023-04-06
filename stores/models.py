from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'
