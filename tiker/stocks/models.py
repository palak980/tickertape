from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_choice=(
        ('r','RELIANCE'),
        ('l','LICI'),
        ('i','IOC'),
        ('s','SBIN'),
        ('t','TATASTEEL'),
    )
    stock=models.CharField(max_length=1, choices=stock_choice)