from django.urls import path
from store import views

urlpatterns = [
    path('products', views.products_list, name='products_list'),
    path('replenish/<int:count>', views.replenish_stock, name='replenish_stock'),
]