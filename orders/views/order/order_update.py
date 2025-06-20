from rest_framework import generics #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from orders.models import Order
from orders.serializers.order.order_update import OrderStatusUpdateSerializer
from users.permissions import IsAdminOrSuperUser

class OrderStatusUpdateThrottle(UserRateThrottle):
    scope = 'order_update'

class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusUpdateSerializer
    permissions_classes = [IsAdminOrSuperUser]
    throttle_classes = [OrderStatusUpdateThrottle]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.none()