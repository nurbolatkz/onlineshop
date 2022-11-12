from django.db import models
from shop.models import Shop
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.IntegerField(default=100)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    update_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name
 