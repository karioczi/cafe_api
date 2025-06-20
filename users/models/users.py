from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )

    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='client'
        )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def reactivate_if_possible(self):
        from django.utils import timezone
        from datetime import timedelta

        if self.deactivated_at:
            delta = timezone.now() - self.deactivated_at
            if delta <= timedelta(days=15):
                self.is_active = True
                self.deactivated_at = None
                self.save()
                return True
        return False
