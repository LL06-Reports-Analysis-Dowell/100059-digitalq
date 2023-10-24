from django.contrib import admin
from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('orders/',views.order_list),
    path('orders/<int:id>', views.order_detail),

    ## dish list 
    path('targeted_population/', views.targeted_populations),
    path('post_population/', views.post_populations), # create new dish
    path('update_population/<str:pk>/', views.update_dish), # update dish info
    # retrive dish data
    path('population/', views.population), # retrive all dish
    path('population/eventid/', views.get_eventid_wise_dish), # retrive eventid_wise single dish
    path('population/type/', views.get_same_type_dish_order), # Retrieve Dish list by dish type
    path('population/dish_code/', views.get_dish_code_type_dish_order), # Retrieve Dish list by dish code
    path('population/dish_id/', views.get_id_wise_dish), # Retrieve id wise dish

    path('payload/', views.payload),
    path('payload/<int:number>', views.payload_param),
    path('connection/', views.connection),
    
    path('create_event/', views.create_events), # for testing 

]

urlpatterns = format_suffix_patterns(urlpatterns)



