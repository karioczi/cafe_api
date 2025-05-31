from rest_framework import serializers #type:ignore
from orders.models import Order

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

        def validate_quantity(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    'Quantity must be greater than zero'
                )
            return value