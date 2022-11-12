from rest_framework import serializers
from product.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id',
                  'name')
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.update_counter += 1
        instance.save()
        return instance

class ProductListCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'shop',
                  'category')


    def create(self, validated_data):
        try:
            product= Product.objects.create(**validated_data)
            return product

        except Exception as e:
            raise serializers.ValidationError({'detail': e})
    

class ProdcutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        field = ('id', 'name')


class ProdcutUpdateCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'update_counter')
