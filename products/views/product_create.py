from rest_framework import generics #type:ignore
from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsSuperUser

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUser]
    throttle_classes = []