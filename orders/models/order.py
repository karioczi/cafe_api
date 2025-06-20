from django.db import models
from django.db.models import Sum, F
from django.conf import settings
from products.models import Product

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In progress'),
        ('failed', 'Failed'),
        ('done', 'Done'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )
    
    products = models.ManyToManyField(
        Product,
        through='OrderItem',
        related_name='orders'
    )

    def total_sum(self):
        return self.order_items.aggregate(
            total=Sum(F('quantity') * F('price_at_order'))
        )['total'] or 0

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"