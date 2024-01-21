from django.contrib import admin
from django.urls import path
from . import views#import views from the current directory 

urlpatterns = [
    path('', views.index, name='home') #It's the root url and it renders views.index in the name of home
]
