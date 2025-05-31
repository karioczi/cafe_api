from rest_framework import serializers #type:ignore
from orders.models import Order
from products.serializers import ProductSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDetailSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'email', 
                  'first_name', 
                  'last_name'
        ]

class OrderDetailSerializer(serializers.ModelSeriliazer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'products',
                  'quantity',
                  'status',
                  'created_at',
                  'updated_at',
                  'user'
                  ]