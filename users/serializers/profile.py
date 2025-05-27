from django.contrib.auth import get_user_model
from rest_framework import serializers #type:ignore[import]

User = get_user_model()

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
        read_only_fields = ['email']
        