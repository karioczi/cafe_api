from rest_framework import serializers #type:ignore
from orders.models import OrderItem

class OrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Quantity must be greater than zero'
            )
        product = self.instance.product if self.instance else None
        f'not enough {product.name}, available {product.quantity}'
        if product and value > product.quantity:
            raise serializers.ValidationError(
                f'Not enough {product.name}, available {product.quantity}.'
            )
        
        return value