from rest_framework import serializers
from .models import *
from .serializers import *
class pataniserializer(serializers.ModelSerializer):
    class Meta:
        model=patani
        field="__all__"
        
    
        
    
    
