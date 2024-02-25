from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
 
# Create your views here.
@api_view(['POST'])
def profileview(request):
    serializer=ProfileSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):  
            serializer.save()
    return Response(serializer.data)

