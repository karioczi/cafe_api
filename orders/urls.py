from django.urls import path
from .views import (
    OrderCreateView,
    OrderDeleteView,
    OrderDetailView,
    OrderListView,
    OrderStatusUpdateView,
    OrderItemUpdateView,
    OrderItemDeleteView
)

urlpatterns = [
     path('order-create/', OrderCreateView.as_view(), name='order-create'),
     path('order-delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
     path('order-detail/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
     path('order/', OrderListView.as_view(), name='order-list'),
     path('order-status/<int:pk>/', OrderStatusUpdateView.as_view(), name='order-status'),
     path('order-items-update/<int:pk>/', OrderItemUpdateView.as_view(), name='order-items-update'),
     path('order-items-delete/<int:pk>', OrderItemDeleteView.as_view(), name='order-items-delete')
]
