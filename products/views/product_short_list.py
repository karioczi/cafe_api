from rest_framework import generics #type:ignore
from products.models import Product
from products.serializers import ProductShortListSerializer
from users.permissions import IsAllowAny

class ProductShortListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductShortListSerializer
    permission_classes = [IsAllowAny]
    pagination_class = None