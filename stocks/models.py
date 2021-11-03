from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=50)
    price = models.TextField()
    rating = models.CharField(max_length=1)