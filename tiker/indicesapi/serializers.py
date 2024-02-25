from indicesapi.models import Indices
from rest_framework import serializers

class IndiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Indices
        fields='__all__'
        
