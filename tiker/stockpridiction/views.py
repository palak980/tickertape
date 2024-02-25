from django.shortcuts import render
import streamlit as st
from datetime import date
import yfinance as yahooFinance
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def snippet_list(request):
    if request.method == 'POST':
        stock=request.data.get('stock')
        if stock=='RELIANCE':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('RELIANCE.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())

        if stock == 'LICI':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('LICI.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
        
        if stock=='IOC':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('IOC.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
            
        
        if stock=='SBIN':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('SBIN.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
            
        
        if stock=='INFY':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('INFY.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())

        if stock=='TATASTEEL':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('TATASTEEL.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
        
        if stock=='TCS':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('TCS.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())

        if stock=='HDFC':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('HDFC.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
        
        if stock=='HDFCBANK':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('HDFCBANK.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
        
        if stock=='HINDUNILVR':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('HINDUNILVR.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
        
        if stock=='ICICIBANK':
            START = "2015-01-01"
            TODAY = date.today().strftime("%Y-%m-%d")

            stocks = ('ICICIBANK.NS')
            
            period =365

            def load_data(ticker):
                data = yahooFinance.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                return data

            data = load_data(stocks)

            # print(data.tail())

            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            forecast = m.predict(future)

            return Response (forecast.tail())
  