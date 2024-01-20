from django.urls import path, include
from . import views

app_name = 'feeds'

urlpatterns = [
    path('', views.home, name='home'),
    
]

