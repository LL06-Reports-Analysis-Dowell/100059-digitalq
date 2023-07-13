from django.contrib import admin
from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('orders/',views.order_list),
    path('orders/<int:id>', views.order_detail),
    path('api/population/', views.population),
    path('api/payload/', views.payload),
    path('api/payload/<int:number>', views.payload_param),
    path('api/targeted_population/', views.targeted_populations),
    path('api/connection/', views.connection),
    path('api/post_population/', views.post_populations),
    path('api/post_order/', views.post_orders),
    path('api/create_event/', views.create_events),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)