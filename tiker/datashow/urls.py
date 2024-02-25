from django.urls import path
from . import views

urlpatterns = [
    path('stock',views.stockview),
    path('crypto',views.cryptoview),
    path('future',views.Trading)
]
    