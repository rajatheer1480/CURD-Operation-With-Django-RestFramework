
from django.contrib import admin
from .models import Customer,Product
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['product_name','mobile','city','state']
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields =['product_name','brand']
    list_display =['id','name','brand','category','selling_price','description','image']

