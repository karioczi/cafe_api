from rest_framework import serializers #type:ignore
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['role']