from rest_framework import serializers #type:ignore
from orders.models import Order
from orders.serializers.order_item.order_item_detail import OrderItemSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'email', 
                  'first_name', 
                  'last_name'
        ]

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id',
                  'status',
                  'total_sum',
                  'created_at',
                  'updated_at',
                  'user',
                  'order_items'
                  ]