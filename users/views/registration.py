from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from drf_spectacular.utils import extend_schema #type:ignore
from django.contrib.auth import get_user_model
from users.serializers.registration import RegistrationSerializer
from users.serializers.profile import ProfileSerializer

User = get_user_model()

class RegistrationThrottle(UserRateThrottle):
    scope = 'registration'

@extend_schema(
    request=RegistrationSerializer,
    responses={201: ProfileSerializer}
)

class RegistrationView(APIView):
    throttle_classes = [RegistrationThrottle]
    permission_classes = []

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        profile_data = ProfileSerializer(user).data
        
        return Response(
            {'message':'Registration was successful', 'user': profile_data},
            status=status.HTTP_201_CREATED
        )