from django.shortcuts import render
from . models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import numpy as np
import pandas as pd
import yfinance as yf
import json
import requests
import cryptocompare
# Defining Binance API URL
@api_view(['POST'])
def cryptoview(request):

    data=cryptocompare.get_price(['BTC', 'ETH','USDT','BNB','DOT','TRX','SOL','TON','ATOM','USDT'])
    adddata=cryptomodel.objects.create(cryptoname=data)
    return Response(cryptocompare.get_price(['BTC', 'ETH','USDT','BNB','DOT','TRX','SOL','TON','ATOM','USDT']))
