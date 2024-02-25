from.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
import yfinance as yf

@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name')
    if value=="EURUSD=X":
        value=="EURUSD=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="EURUSD=X",period='id',interval='1m')
    print(show)
    return Response(show)


@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name')
    if value=="USDMXN=X":
        value=="USDMXN=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="USDMXN=X",period='id',interval='1m')
    print(show)
    return Response(show)
      



@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name') 
    if value=="USDCHF=X":
        value=="USDCHF=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="USDCHF=X",period='id',interval='1m')
    print(show)
    return Response(show)



@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name') 
    if value=="GBPUSD=X":
        value=="GBPUSD=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="GBPUSD=X",period='id',interval='1m')
    print(show)
    return Response(show)

@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name') 
    if value=="USDCAD=X":
        value=="USDCAD=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="USDCAD=X",period='id',interval='1m')
    print(show)
    return Response(show)



@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name') 
    if value=="NZDUSD=X":
        value=="NZDUSD=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="NZDUSD=X",period='id',interval='1m')
    print(show)
    return Response(show)        

@api_view(['POST'])
def Trading(request):
    value=request.data.get('currency_name') 
    if value=="AUDUSD=X":
        value=="AUDUSD=X"
    value=request.data.get('currency_name')
    show=yf.download(tickers="AUDUSD=X",period='id',interval='1m')
    print(show)
    return Response(show) 



                      
 







    

