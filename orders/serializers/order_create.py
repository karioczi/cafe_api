from rest_framework import serializers #type:ignore
from orders.models import Order, Product

class OrderCreateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all()
    )

    class Meta:
        model = Order
        fields = ['products', 'quantity', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        return order