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
    path('api/delete_population/<str:pk>/', views.delete_dish), # delete dish
    path('api/update_population/<str:pk>/', views.update_dish), # update dish info
    # retrive dish data
    path('api/population/', views.population), # retrive all dish
    path('api/population/eventid/', views.get_eventid_wise_dish), # retrive eventid_wise single dish
    path('api/population/type/', views.get_same_type_dish_order), # Retrieve Dish list by dish type
    path('api/population/dish_code/', views.get_dish_code_type_dish_order), # Retrieve Dish list by dish code
    path('api/population/dish_id/', views.get_id_wise_dish), # Retrieve id wise dish

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



