from rest_framework import generics #type:ignore
from products.models import Product
from products.serializers import ProductShortListSerializer
from users.permissions import IsAllowAny

class ProductShortListView(generics.ListAPIView):
    serializer_class = ProductShortListSerializer
    permission_classes = [IsAllowAny]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Product.objects.all()
        return Product.objects.filter(is_active=True)