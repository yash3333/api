from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('add/',user),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),    

    
      
]