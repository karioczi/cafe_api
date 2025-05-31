from rest_framework import generics #type:ignore
from rest_framework.permissions import IsAuthenticated #type:ignore
from orders.models import Order
from orders.serializers import OrderUpdateSerializer

class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)