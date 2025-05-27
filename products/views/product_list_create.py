from rest_framework import generics, permissions #type:ignore
from products.models import Product
from products.permissions.product_permissions import IsAdminOrReadOnly
from products.serializers.product import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]