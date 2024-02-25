from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mftool import Mftool
from .models  import *
from .serializers import *

@api_view(['POST'])
def mutualview(request):
    obj = Mftool()
    choices=request.data.get('choices')
    if choices=='Reliance Fixed Horizon Fund':
        a = obj.get_scheme_quote('126703')
        return Response(a)
    if choices=='Axis Banking & PSU Debt Fund - Regular Plan - Monthly IDCW':
        b = obj.get_scheme_quote('117449')
        return Response(b)
    if choices=='UTI Fixed Term Income Fund':
        c = obj.get_scheme_quote('150970')
        return Response(c)
    if choices=='SBI Fixed Maturity Plan':
        d = obj.get_scheme_quote('149822')
        return Response(d)
    if choices=='Aditya Birla Sun Life Banking & PSU Debt fund':
        e = obj.get_scheme_quote('119551')
        return Response(e)
    if choices=='DSP Banking & PSU Debt fund':
        f= obj.get_scheme_quote('124182')
        return Response(f)