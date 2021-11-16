from django.urls import path, include
from django.contrib import admin

from .views import FoodCreateView, FoodDeleteView, FoodShowView, FoodUpdateView



urlpatterns = [
    path('createfood', FoodCreateView.as_view(), name='createfood'),
    path('updatefood/<pk>', FoodUpdateView.as_view(), name='updatefood'),
    path('deletefood', FoodDeleteView.as_view(), name='deletefood'),
    path('foods', FoodShowView.as_view(), name='foods'),
    
]