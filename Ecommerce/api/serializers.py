from itertools import product
from django.contrib.auth.models import User
from .models import Customer,Product
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer




class ProductSerializer(serializers.ModelSerializer):
    # user= serializers.StringRelatedField()
    class Meta:
        model = Product
        fields= ['id','name','brand','category','selling_price','description','image']


class CustomerSerializer(serializers.ModelSerializer):
    product_name = ProductSerializer(many=False, read_only=True)
    user = serializers.StringRelatedField()
 
    class Meta:
        model = Customer
        fields = ['id','user','mobile','city','state','product_name']
    
