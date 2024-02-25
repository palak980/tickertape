from django.db import models

class Currencies(models.Model):
    currency_name=models.CharField(max_length=100)