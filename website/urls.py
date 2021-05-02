from django.contrib import admin
from django.urls import path 
from website import views

urlpatterns = [
     path('', views.index, name='index'),
     path('contact', views.contact, name='contact'),
]
