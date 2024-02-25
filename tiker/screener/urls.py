from django.urls import path
from screener import views



urlpatterns = [
    path('', views.getdata,)
]