from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from shop.serializers import ShopSerializer
from shop.models import Shop
from product.models import Product
from product.serializers import ProductSerializer, ProductListCreateSerializer, ProdcutUpdateCounterSerializer
from onlineshop.utils import CustomPagination


# Create your views here.
class ShopViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Shop.objects.all()
        paginator = CustomPagination()
        pages = paginator.paginate_queryset(queryset, request)
        if pages is not None:
            serializer = ShopSerializer(pages, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = ShopSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)
    

    @action(["get"], detail=True)
    def products(self, request, shop_pk=None, category_pk=None):
        if category_pk:
            products = Product.objects.filter(category_id=category_pk, shop_id=shop_pk)
        else:
            products = Product.objects.filter(shop_id=shop_pk)
        paginator = CustomPagination()
        pages = paginator.paginate_queryset(products, request)
        if pages is not None:
            serializer = ProductSerializer(pages, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)


    @action(["get"], detail=True)
    def update_counter(self, request, shop_pk=None, category_pk=None):
            if category_pk:
                products = Product.objects.filter(category_id=category_pk, shop_id=shop_pk)
            else:
                products = Product.objects.filter(shop_id=shop_pk)
            paginator = CustomPagination()
            pages = paginator.paginate_queryset(products, request)
            
            if pages is not None:
                serializer = ProdcutUpdateCounterSerializer(pages, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)



    def create(self,request, shop_pk=None, category_pk=None):
        if shop_pk and category_pk is not None:
            data = request.data
            for el in data:
                el['shop'] = shop_pk
                el['category'] = category_pk
            serializer = ProductListCreateSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
