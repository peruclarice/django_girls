from django.urls import path
from .views import *

urlpatterns = [
    path('all-products', get_all_products),
    path('all-products/<int:id>/', get_product_by_id),
    path('products/create', create_product),
    path('products/json-products', get_all_products_json)
]