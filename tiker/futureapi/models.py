from django.db import models

# Create your models here.
class Currencies(models.Model):
    currency_name=models.CharField(max_length=100)