from rest_framework import generics #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from orders.models.order import Order
from orders.serializers.order.order_list import OrderListSerializer
from users.permissions import IsAuthenticated

class OrderListThrottle(UserRateThrottle):
    scope = 'order_list'

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [OrderListThrottle]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all().order_by('-created_at')
        return Order.objects.filter(user=self.request.user).order_by('-created_at')