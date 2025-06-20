from rest_framework import generics #type:ignore
from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsAdminOrSuperUser

class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrSuperUser]
    throttle_classes = []