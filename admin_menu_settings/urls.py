from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    create_branches,
    get_branch_list_view,
)
urlpatterns = [
    path('create-branch/', create_branches),
    path('branch/', get_branch_list_view)

]

# urlpatterns = format_suffix_patterns(urlpatterns)