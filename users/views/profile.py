from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from django.contrib.auth import get_user_model
from users.permissions import IsAuthenticated
from users.serializers.profile import ProfileSerializer

User = get_user_model()

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
