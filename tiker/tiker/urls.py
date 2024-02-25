
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/',include('stocks.urls')),
    path('forex/',include('forexapi.urls')),
    path('future/',include('futureapi.urls')),
    path('mutual/',include('mutual.urls')),
    path('cryptocurrency/',include('cryptocurrency.urls')),
    path('profile/',include('profile.urls')),
    path('screener/',include('screener.urls')),
    path('social/',include('social.urls')),
    path('datashow/',include('datashow.urls')),
    path('news/',include('Newsstock.urls')),
    path('indices/',include('indicesapi.urls')),
    path('priciction/',include('stockpridiction.urls')),
    path('marketmood/',include('api.urls')),


]
