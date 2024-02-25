from django.db import models

# Create your models here.
class choice(models.Model):
  
    stock=models.CharField(max_length=100)