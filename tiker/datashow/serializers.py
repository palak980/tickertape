from rest_framework import serializers
from .models import * 

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = stockmodel
        fields='__all__'
        
class cryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = cryptomodel
        fields='__all__'