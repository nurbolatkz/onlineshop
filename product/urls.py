from django.urls import path
from product import views

productDetail = views.ProductViewSet.as_view({'get':'retrieve', 'put':'update'})


urlpatterns = [
    path('<int:shop_id>/categories/<int:category_id>/<int:product_id>', productDetail)
]
