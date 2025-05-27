from rest_framework import serializers #type:ignore[import]
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(validators=[validate_password]) 
    token = serializers.CharField()
    uidb64 = serializers.CharField()
    