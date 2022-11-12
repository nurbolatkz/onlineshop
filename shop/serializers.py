from rest_framework import serializers
from shop.models import Shop, ShopCategory

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id',
                  'name',  
                  'address', 
                  'phone_number', 
                  'category', 
                  'rating', 
                  'created_at',
                  'updated_at')


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = ('name')
