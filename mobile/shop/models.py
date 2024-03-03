from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    pic = models.FileField(upload_to='shop/pic', null=True, blank=True)
    price = models.TextField()


class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    cover = models.FileField(upload_to='shop/cover', null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    pic = models.FileField(upload_to='shop/pic', null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.title
    def subtotal(self):
        return self.quantity*self.product.price

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noofitems = models.IntegerField()
    adress=models.TextField()
    phone=models.CharField(max_length=30)
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status = models.CharField(max_length=20,default="pending")
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
class Account(models.Model):

    accntno=models.CharField(max_length=30)
    accnttype=models.CharField(max_length=30)
    amount=models.IntegerField()
    def __str__(self):
        return self.accntno

