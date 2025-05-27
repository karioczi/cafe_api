from django.urls import path
from products.views.product_detail import ProductDetailView
from products.views.product_list_create import ProductListCreateView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]