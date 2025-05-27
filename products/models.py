from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name