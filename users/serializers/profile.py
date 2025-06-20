from rest_framework import serializers #type:ignore[import]
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 
                  'role',
                  'username', 
                  'email', 
                  'first_name', 
                  'last_name',
                  'date_joined'
        ]
        read_only_fields = ['email']
        

