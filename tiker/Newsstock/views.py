from django.shortcuts import render
import requests
import pandas as pd
from bs4 import BeautifulSoup
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from cleantext import clean

# Create your views here.
@api_view(['GET'])
def getdata(request):
    
    request.method == 'GET'
    htmldata = requests.get("https://economictimes.indiatimes.com/markets/stocks/live-blog/bse-sensex-today-live-nifty-stock-market-updates-27-october-2022/liveblog/95109430.cms")
    soup= BeautifulSoup(htmldata.content, 'html5lib')
    news = soup.find("div", {"class" : "clearfix main_container"})
    stock_news = news.text
    #print(stock_news)
    clr =(clean(text=stock_news,
            fix_unicode=True,
            to_ascii=True,
            lower=True,
            no_line_breaks=False,
            no_urls=False,
            no_emails=False,
            no_phone_numbers=False,
            no_numbers=False,
            no_digits=False,
            no_currency_symbols=False,
            no_punct=False,
            replace_with_punct="",
            replace_with_url="This is a URL",
            replace_with_email="Email",
            replace_with_phone_number="",
            replace_with_number="123",
            replace_with_digit="0",
            replace_with_currency_symbol="$",
            lang="en"
            ))
    return JsonResponse(
        {"news from times of india":clr},
        safe=False)
    return Response(stock_news)




