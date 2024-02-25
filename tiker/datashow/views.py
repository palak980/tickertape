from django.shortcuts import render
from . models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import yfinance as yf
import cryptocompare
# Create your views here.

@api_view(['POST'])
def stockview(request):
    model=request.data.get('stockname')
    
    if model=='TCS':
        data = yf.download(tickers='TCS', period='1d', interval='1m')
        return Response(data) 
    
    if model=='INFY':
        data = yf.download(tickers='INFY', period='1d', interval='1m')
        return Response(data)
    
    if model=='AAPL':
        data = yf.download(tickers='AAPL', period='1d', interval='1m')
        return Response(data)

    if model=='ACN':
        data = yf.download(tickers='ACN', period='1d', interval='1m')
        return Response(data)
    
    if model=='CTSH':
        data = yf.download(tickers='CTSH', period='1d', interval='1m')
        return Response(data)
    
    
 
# Defining Binance API URL
@api_view(['POST'])
def cryptoview(request):

    data=cryptocompare.get_price(['BTC', 'ETH','USDT','BNB','DOT','TRX','SOL','TON','ATOM','USDT'])
    adddata=cryptomodel.objects.create(cryptoname=data)
    return Response(cryptocompare.get_price(['BTC', 'ETH','USDT','BNB','DOT','TRX','SOL','TON','ATOM','USDT']))



@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name')
    if value=="ZG":
        show=yf.download(tickers="ZG",period='id',interval='1m')
        print(show)
        return Response(show)

    if value=="ZI":
        show=yf.download(tickers="ZI",period='id',interval='1m')
        print(show)
        return Response(show)   

    if value=="AEO":
        show=yf.download(tickers="AEO",period='id',interval='1m')
        print(show)
        return Response(show)    

    
    if value=="B":
        show=yf.download(tickers="B",period='id',interval='1m')
        print(show)
        return Response(show)    

    if value=="RS":
        show=yf.download(tickers="RS",period='id',interval='1m')
        print(show)
        return Response(show)    
             
    if value=="CC":
        show=yf.download(tickers="CC",period='id',interval='1m')
        print(show)
        return Response(show)    
                      
    if value=="HOV":
        show=yf.download(tickers="HOV",period='id',interval='1m')
        print(show)
        return Response(show)    
                               
    if value=="C":
        show=yf.download(tickers="C",period='id',interval='1m')
        print(show)
        return Response(show)    

    if value=="BAR":
        show=yf.download(tickers="BAR",period='id',interval='1m')
        print(show)
        return Response(show)

    if value=="GDO":
        show=yf.download(tickers="GDO",period='id',interval='1m')
        print(show)
        return Response(show)    
                     
                                                 
         
     

 
