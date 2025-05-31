from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=150, 
        blank=True, 
        null=True, 
        unique=False
    )
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='client'
    )
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email


