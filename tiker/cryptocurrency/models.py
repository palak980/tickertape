from django.db import models

# Create your models here
class cryptomodel(models.Model):
    
    cryptoname=models.CharField(max_length=100)
    