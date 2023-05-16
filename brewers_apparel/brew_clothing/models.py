from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
class Shopping_cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    
    
    
