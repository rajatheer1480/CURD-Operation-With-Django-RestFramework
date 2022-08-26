from unicodedata import category
from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router =DefaultRouter()

router.register('customerapi',views.Customer_View,basename='customer'),
router.register('productapi',views.Product_View,basename='product'),

urlpatterns = [
    path('',views.Home_View.as_view(),name='home'),
    path('api/v1/',include(router.urls)), 
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
    ]