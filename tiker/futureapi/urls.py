from django.urls import path
from . import views
urlpatterns = [
    path('trading/',views.trading)
]