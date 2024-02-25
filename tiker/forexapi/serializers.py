from .models import *
from rest_framework import serializers

class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Currencies
        fields=['currency_name']