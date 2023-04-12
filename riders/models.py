from django.db import models

# Create your models here.
class Rider(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name}"
