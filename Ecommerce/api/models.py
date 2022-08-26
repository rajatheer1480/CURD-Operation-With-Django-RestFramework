
from django.db import models

from django.contrib.auth.models import User
# Create your models here.



class Product(models.Model):
    category =(
        ('Mobile','Mobile'),
        ('Laptop','Laptop'),
        ('Shoes','Shoes'),
        ('Watch','Watch'),
        ('Top Wear','Top Wear'),
        ('Down Wear','Down Wear'),
    )

    name = models.CharField(max_length=255)
    selling_price =models.IntegerField()
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=300)
    category = models.CharField(choices=category,max_length=30)
    image = models.ImageField(upload_to ='prod_img')


    def __str__(self):
        return "#ID %s-%s" %(self.name,self.brand)

    class Meta:
        verbose_name ='Product'
        verbose_name_plural='Products'


 

###########-------CATEGORY-------#########

class Customer(models.Model):
    State = (
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CT','Chhattisgarh'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jammu and Kashmir'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OR','Odisha'),
    ('PB','Punjab'),
    ('RJ','Rajasthan'),
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),
    ('TG','Telangana'),
    ('TR','Tripura'),
    ('UT','Uttarakhand'),
    ('UP','Uttar Pradesh'),
    ('WB','West Bengal'),
    ('AN','Andaman and Nicobar Islands'),
    ('CH','Chandigarh'),
    ('DD','Daman and Diu'),
    ('DN','Dadra and Nagar Haveli'),
    ('DL','Delhi'),
    ('LD','Lakshadweep'),
    ('PY','Puducherry'),
) 

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='owner')
    product_name = models.ForeignKey(Product,on_delete=models.CASCADE, default=None, null=True,blank=True,related_name='product_name') 
    mobile = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255,choices=State, null=True, blank=True)


    def __str__(self):
        return "#ID %s-%s" %(self.user,self.city)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
