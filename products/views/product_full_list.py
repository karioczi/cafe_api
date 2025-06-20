from rest_framework import generics #type:ignore
from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsAdminOrSuperUser

class ProductFullListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrSuperUser]
    pagination_class = None