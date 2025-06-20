from rest_framework import generics #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from orders.models import Order
from orders.serializers.order.order_create import OrderCreateSerializer
from users.permissions import IsAuthenticated

class OrderCreateThrottle(UserRateThrottle):
    scope = 'order_create'

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [OrderCreateThrottle]

    def perform_create(self, serializer):
        serializer.save()
        