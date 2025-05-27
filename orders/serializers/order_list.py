from rest_framework import serializers #type:ignore
from orders.models import Order
from products.serializers import ProductSerializer

class OrderListSerializer(serializers.ModeSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id',
                  'user',
                  'status',
                  'created_at',
                  'products'
        ]