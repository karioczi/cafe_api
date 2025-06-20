from rest_framework import serializers #type:ignore
from orders.models.order import Order
from orders.serializers.order_item.order_item_detail import OrderItemSerializer

class OrderListSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(source='order_items', many=True, read_only=True)
    user = serializers.StringRelatedField()
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id',
                  'user',
                  'status',
                  'created_at',
                  'products',
                  'total_sum'
        ]

    def get_total_sum(self, obj):
        return obj.total_sum()