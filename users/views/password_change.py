from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from users.serializers.password_change import PasswordChangeSerializer
from users.permissions import IsAuthenticated

class PasswordChangeThrottle(UserRateThrottle):
    scope = 'password_change'

class PasswordChangeView(APIView):
    throttle_classes = [PasswordChangeThrottle]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password updated successfully'}, status=status.HTTP_200_OK)
        