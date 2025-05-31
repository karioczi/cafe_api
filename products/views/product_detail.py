from rest_framework.generics import RetrieveUpdateDestroyAPIView #type:ignore
from rest_framework.permissions import IsAdminUser, AllowAny #type:ignore
from products.models import Product
from products.serializers.product import ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return[AllowAny()]
        return [IsAdminUser()]
    