from django.contrib import admin
from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('orders/',views.order_list),
    path('orders/<int:id>', views.order_detail),

    # dis list 
    path('api/targeted_population/', views.targeted_populations),
    path('api/post_population/', views.post_populations),
    path('api/population/', views.population),
    path('api/population/<str:dish_event_id>', views.get_single_dish_order),
    path('api/population/type/<str:dish_order_type>', views.get_same_type_dish_order),

    path('api/payload/', views.payload),
    path('api/payload/<int:number>', views.payload_param),
    path('api/connection/', views.connection),
    path('api/post_order/', views.post_orders),
    path('api/create_event/', views.create_events), #for testing 

]

urlpatterns = format_suffix_patterns(urlpatterns)
