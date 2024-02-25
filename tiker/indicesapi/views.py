from django.shortcuts import render
from indicesapi.models import Indices
from indicesapi.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import yfinance as yahooFinance
# Create your views here.
@api_view(['POST'])
def indices_list(request):
    if request.method=="POST":
        indices=request.data.get('indices')

        if indices=='NIFTY':
            nifty_data=yahooFinance.download(tickers="^NSEI",period='id',interval='1m')
            # print(nifty_data)
            return Response(nifty_data)
        
        if indices == 'SENSEX':
            # S&P BSE SENSEX INDEX
            nifty_data=yahooFinance.download(tickers="^BSESN",period='id',interval='1m')
            # print(nifty_data)
            return Response(nifty_data)
        
        if indices=='DFMGI':
            # DFM General Index
            nifty_data=yahooFinance.download(tickers="DFMGI.AE",period='id',interval='1m')
            # print(nifty_data)
            return Response(nifty_data)
        
        if indices == 'DAX':
            # Global X DAX Germany ETF
            nifty_data=yahooFinance.download(tickers="DAX",period='id',interval='1m')
            # print(nifty_data)
            return Response(nifty_data)
        
        if indices=='BSE500':
            nifty_data=yahooFinance.download(tickers="BSE-500.BO",period='id',interval='1m')
            # print(nifty_data)
            return Response(nifty_data)
        


