from django.contrib import admin
from django.urls import path
from shop import views

shop_list = views.ShopViewSet.as_view({'get': 'list'})
shopInfo = views.ShopViewSet.as_view({'get': 'retrieve'})
products_by_category = views.ShopViewSet.as_view({'get': 'products', 'post':'create'})
updateDetail = views.ShopViewSet.as_view({'get':'update_counter'})

urlpatterns = [
    path('shops/', shop_list),
    path('shops/<int:pk>/', shopInfo),
    path('<int:shop_pk>/categories/<int:category_pk>', products_by_category),
    path('<int:shop_pk>/categories/<int:category_pk>/updates/', updateDetail)
]
