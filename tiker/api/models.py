from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name=models.CharField(max_length=100)