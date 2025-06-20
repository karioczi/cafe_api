from rest_framework import serializers #type:ignore
from django.contrib.auth import get_user_model
from orders.serializers import OrderListSerializer

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id', 
            'email', 
            'username', 
            'role', 
            'is_active', 
            'date_joined',
            'last_login',
            'orders',
        ]

    def get_orders(self, obj):
        orders = obj.orders.all()
        return OrderListSerializer(orders, many=True).data