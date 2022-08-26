from re import template
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from rest_framework import viewsets
from .models import Customer, Product
from rest_framework import generics
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .serializers import CustomerSerializer,ProductSerializer
# Create your views here.

class Home_View(View):
    template_name='api/home.html'
    def get(self,request):
        return render(request,self.template_name)


class Customer_View(viewsets.ModelViewSet):
    serializer_class =  CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    


class Product_View(viewsets.ModelViewSet):
    serializer_class =  ProductSerializer
    queryset = Product.objects.all().order_by('name')
    permission_classes = [IsAuthenticated,IsAdminUser]
   




  

    