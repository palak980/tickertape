from django.urls import path
from social import views
urlpatterns = [
    path('', views.profileview, name='home'),
    
]
