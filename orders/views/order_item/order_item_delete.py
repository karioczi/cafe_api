from rest_framework import generics #type:ignore
from rest_framework.exceptions import ValidationError #type:ignore
from orders.models import OrderItem
from users.permissions import IsAdminOrSuperUser

class OrderItemDeleteView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    permission_classes = [IsAdminOrSuperUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return OrderItem.objects.all()
        return OrderItem.objects.filter(order__user=user)
    
    def perform_destroy(self, instance):
        forbidden = ['in_progress', 'failed', 'done']
        user = self.request.user
        if instance.order.status in forbidden and not user.is_superuser:
            raise ValidationError(
                f'You cant delete order which have status: {", ".join(forbidden)}'
            )
        instance.delete() 