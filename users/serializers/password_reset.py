from rest_framework import serializers #type:ignore[import]
from django.contrib.auth.password_validation import validate_password

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, validators=[validate_password]) 
    token = serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)
    