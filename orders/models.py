from django.db import models
from django.conf import settings
from products.models import Product
    
class Order(models.Model):
    products = models.ManyToManyField('products.Product')
    
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In progress'),
        ('failed', 'Failed'),
        ('done', 'Done'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='open'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"
    
