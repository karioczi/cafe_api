from django.contrib.auth import authenticate
from rest_framework import serializers #type:ignore[import]

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError(
                    'Wrong email or password'
                )
        else:
            raise serializers.ValidationError(
                'Email and password are required'
            )
        attrs['user'] = user
        return attrs