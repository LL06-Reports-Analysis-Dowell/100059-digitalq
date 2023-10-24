from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    post_orders,
    get_dish_order_view,
    get_order_by_coupon_view
)

urlpatterns = [
    path('api/post_order/', post_orders), # create order
    path('order/', get_dish_order_view), # get all orders 
    path('order/coupon/', get_order_by_coupon_view), # get orders by coupon
    
]