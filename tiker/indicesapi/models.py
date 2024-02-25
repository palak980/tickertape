from django.db import models

# Create your models here.
class Indices(models.Model):
    indices_choice=(
        ('n','NIFTY'),
        ('b','SENSEX'),
        ('d','DFMGI'),
        ('a','DAX'),
        ('n','BSE500'),
        
    )
    indices=models.CharField(max_length=1,choices=indices_choice)