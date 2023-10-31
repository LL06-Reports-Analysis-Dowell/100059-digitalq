from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    create_branches,
)
urlpatterns = [
    path('create-branch/', create_branches)

]

# urlpatterns = format_suffix_patterns(urlpatterns)