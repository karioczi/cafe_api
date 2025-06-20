from rest_framework import generics #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from orders.models.order import Order
from orders.serializers.order.order_detail import OrderDetailSerializer
from users.permissions import IsAdminOrSuperUser

class OrderDetailThrottle(UserRateThrottle):
    scope = 'order_detail'

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAdminOrSuperUser] 
    throttle_classes = [OrderDetailThrottle]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)