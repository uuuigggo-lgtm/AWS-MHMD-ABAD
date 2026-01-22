from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', product_create, name='product_add'),
    path('edit/<int:id>/', product_update, name='product_edit'),
    path('delete/<int:id>/', product_delete, name='product_delete'),
]