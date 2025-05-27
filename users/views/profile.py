from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework.permissions import IsAuthenticated #type:ignore
from users.serializers.profile import ProfileSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)