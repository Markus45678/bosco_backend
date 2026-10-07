from django.urls import path
from store import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
]