from django.contrib import admin
from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('orders/',views.order_list),
    path('orders/<int:id>', views.order_detail),

    ## dish list 
    path('api/targeted_population/', views.targeted_populations),
    path('api/post_population/', views.post_populations), # create new dish
    # retrive dish data
    path('api/population/', views.population), # retrive all dish
    path('api/population/<str:dish_event_id>', views.get_single_dish_order), # retrive single dish order
    path('api/population/type/', views.get_same_type_dish_order), # Retrieve Dish Order by dish type

    path('api/payload/', views.payload),
    path('api/payload/<int:number>', views.payload_param),
    path('api/connection/', views.connection),

    ## order API
    path('api/post_order/', views.post_orders), # create order
    path('api/order/', views.get_dish_order_view), # get all orders 
    path('api/order/coupon/', views.get_order_by_coupon_view), # get orders by coupon
    path('api/order/queue/', views.get_order_by_queue_view), # get orders by queue
    path('api/create_event/', views.create_events), # for testing 

]

urlpatterns = format_suffix_patterns(urlpatterns)
