from rest_framework import serializers #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework_simplejwt.tokens import RefreshToken #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from drf_spectacular.utils import extend_schema #type:ignore
from users.serializers.login import LoginSerializer

class LoginThrottle(UserRateThrottle):
    scope = 'login'
    
class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    acces = serializers.CharField()

@extend_schema(
    request=LoginSerializer,
    responses={200: TokenSerializer}
)

class LoginView(APIView):
    throttle_classes = [LoginThrottle]
    permission_classes = []

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        