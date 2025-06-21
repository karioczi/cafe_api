from django.db import transaction
from rest_framework import generics #type:ignore
from rest_framework.exceptions import ValidationError #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from users.permissions import IsAdminOrSuperUser
from orders.models import Order

class OrderDeleteThrottle(UserRateThrottle):
    scope = 'order_delete'

class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAdminOrSuperUser]
    throttle_classes = [OrderDeleteThrottle]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)
    
    def perform_destroy(self, instance):
        forbidden = ['in_progress', 'failed', 'done']
        user = self.request.user 

        if instance.status in forbidden and not user.is_superuser:
            raise ValidationError(
                f'You cant delete order which have status: {", ".join(forbidden)}'
            )
        
    
        with transaction.atomic():
            for item in instance.order_items.all():
                product = item.product
                product.quantity += item.quantity
                product.save()
            instance.delete()