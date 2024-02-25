from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import yfinance as yahooFinance




@api_view(['POST'])
def snippet_list(request):
    if request.method == 'POST':
        stock=request.data.get('stock')
        if stock=='RELIANCE':
            reliancs_stocks_data = yahooFinance.download(tickers="RELIANCE.NS",period='id',interval='1m')
            # print(reliancs_stocks_data)
            return Response(reliancs_stocks_data)

        if stock == 'LICI':
            lic_stocks_data =yahooFinance.download(tickers="LICI.NS",period='id',interval='1m')
            # print(lic_stocks_data)
            return Response(lic_stocks_data)
        
        if stock=='IOC':
            indianoil_stocks_data = yahooFinance.download(tickers="IOC.NS",period='id',interval='1m')
            # print(indianoil_stocks_data)
            return Response(indianoil_stocks_data)
        
        if stock=='SBIN':
            sbi_stocks_data = yahooFinance.download(tickers="SBIN.NS",period='id',interval='1m')      
            # print(sbi_stocks_data)
            return Response(sbi_stocks_data)
        
        if stock=='TATASTEEL':
            tatasteel_stocks_data =yahooFinance.download(tickers="TATASTEEL.NS",period='id',interval='1m')
            # print(tatasteel_stocks_data)
            return Response(tatasteel_stocks_data)

       
