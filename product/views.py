from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def retrieve(self, request, shop_id=None, category_id=None, product_id=None):
        if shop_id and category_id and product_id is not None:
            products = Product.objects.filter(shop_id=shop_id, category_id=category_id)
            product = get_object_or_404(products, pk=product_id)
            serializer = ProductSerializer(product)
            
            return Response(serializer.data)


    def update(self, request, product_id=None, *args, **kwargs):
        products = Product.objects.all()
        if not product_id:
            return Response({'Error': 'Update not allowed'})
            
        instance = get_object_or_404(products, pk=product_id)
        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)
    