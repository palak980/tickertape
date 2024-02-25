from django.db import models

# Create your models here.

class stockmodel(models.Model):
    stockname=models.CharField(max_length=100)
    
class cryptomodel(models.Model):
    cryptoname=models.CharField(max_length=100)
    
    
class Currencies(models.Model):
    currency_name=models.CharField(max_length=100)