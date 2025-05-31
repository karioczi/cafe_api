from django.urls import path
from orders.views import (
    OrderCreateView,
    OrderDeleteView,
    OrderDetailView,
    OrderListView,
    OrderUpdateView
)

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-delete/<int:pk>', OrderDeleteView.as_view(), name='order-delete'), 
    path('order-detail/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('order-update/<int:pk>', OrderUpdateView.as_view(), name='order-update')
]
