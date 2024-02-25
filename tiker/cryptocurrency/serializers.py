from rest_framework import serializers
from .models import * 

class cryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = cryptomodel
        fields='__all__'