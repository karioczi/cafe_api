from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework_simplejwt.tokens import RefreshToken #type:ignore
from django.contrib.auth import authenticate
from users.serializers.login import LoginSerializer

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(
            {'detail':'Invalid credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )