from django.contrib import admin

# Register your models here.
from shop.models import Shop, ShopCategory

admin.site.register(Shop)
admin.site.register(ShopCategory)