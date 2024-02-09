from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    
    path('product_details/<pk>',views.shop_details,name='product_details'),
]