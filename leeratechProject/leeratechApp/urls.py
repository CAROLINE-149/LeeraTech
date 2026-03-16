from django.shortcuts import render
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('features/',views.features, name='features'),
    path('about/',views.about, name='about'),
    path('solutions/',views.solutions, name='solutions'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact')
]