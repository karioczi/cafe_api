from rest_framework import serializers #type:ignore[import]
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError(
                'Email and password are required'
            )
        
        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError(
                'Wrong email or password.'
            )
            
        if not user.is_active:
            if user.deactivated_at:
                if not user.reactivate_if_possible():
                    raise serializers.ValidationError(
                        'Account deactivated more than 15 days ago.'
                    )
            else:
                raise serializers.ValidationError(
                    'Account is deactivated.'
                )

        attrs['user'] = user
        return attrs