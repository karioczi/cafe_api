from django.urls import path
from products.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductFullListView,
    ProductShortListView,
    ProductUpdateView,
)

urlpatterns = [
    path('', ProductShortListView.as_view(), name='product-short-list'),
    path('full/', ProductFullListView.as_view(), name='product-full-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
]