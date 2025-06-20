from rest_framework import serializers #type:ignore
from products.models import Product

class ProductShortListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'available']