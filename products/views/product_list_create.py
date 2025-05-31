from rest_framework import generics, permissions #type:ignore
from products.models import Product
from products.permissions import IsAdminOrReadOnly
from products.serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]