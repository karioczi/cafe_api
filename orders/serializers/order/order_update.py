from rest_framework import serializers #type:ignore
from orders.models import Order

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

    def validate_status(self, value):
        allowed = [
            'open', 
            'in_progress', 
            'failed', 
            'done'
        ]

        if value not in allowed:
            raise serializers.ValidationError(
                'Invalid status'
            )
        
        instance = getattr(self, 'instance', None)
        if instance:
            status_order = {
                'open': 0, 
                'in_progress': 1, 
                'failed': 2,
                'done': 3
            }
            current = status_order.get(instance.status)
            new = status_order.get(value)
            if new < current:
                raise serializers.ValidationError(
                    'Status rollback is not allowed'
                )
            
        return value
        