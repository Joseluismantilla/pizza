from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_pizza, name='order_pizza'),
    path('orders/', views.order_list, name='order_list'),
]

