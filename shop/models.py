from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class ShopCategory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE, null=True)
    rating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
        