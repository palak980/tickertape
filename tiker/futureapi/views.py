from.models import *
from rest_framework.response import Response
#from stack_data import Serializer
from rest_framework.decorators import api_view
import yfinance as yf

@api_view(['POST'])
def trading(request):
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
                     
                                                 
         
     

 
