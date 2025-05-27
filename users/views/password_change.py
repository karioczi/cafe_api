from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.permissions import IsAuthenticated #type:ignore
from rest_framework.response import Response #type:ignore
from users.serializers.password_change import PasswordChangeSerializer

class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Password updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 