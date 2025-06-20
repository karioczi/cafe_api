from django.contrib.auth.base_user import BaseUserManager
from typing import Any

class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None, **extra_fields: Any):
        if not email:
            raise ValueError(
                'Email is required'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if not extra_fields.get('is_staff') or not extra_fields.get('is_superuser'):
            raise ValueError(
                'Superuser must have admin privileges.'
            )

        return self.create_user(email, password, **extra_fields)