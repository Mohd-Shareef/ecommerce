from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_id=models.AutoField
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    desc=models.CharField(max_length=300,default=False)
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=False)

    def __str__(self):
        return self.name
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=50,default="")
    area=models.CharField(max_length=300,default="")
    phone=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.name
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=0)
    price=models.PositiveIntegerField(default=0)
    total_price=models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username}'s cart-{self.product.name}"
    
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    price=models.IntegerField(default=0)
    state=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=15,null=True)
    pincode=models.CharField(max_length=200,null=True)
    date_added=models.DateField(auto_now_add=True)


    def __str__(self):
          return self.name   
      
