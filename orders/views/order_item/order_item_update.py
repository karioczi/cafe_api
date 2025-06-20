from rest_framework import generics #type:ignore
from rest_framework.exceptions import ValidationError #type:ignore
from orders.models import OrderItem
from orders.serializers.order_item.order_item_update import OrderItemUpdateSerializer
from users.permissions import IsAuthenticated 

class OrderItemUpdateView(generics.UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return OrderItem.objects.all()
        return OrderItem.objects.filter(order__user=user)
    
    def perform_update(self, serializer):
        instance = self.get_object()
        forbidden = ['in_progress', 'failed', 'done']
        user = self.request.user
        if instance.order.status in forbidden and not user.is_superuser:
            raise ValidationError(
                'Cannot update item for order with this status.'
            )
        serializer.save()