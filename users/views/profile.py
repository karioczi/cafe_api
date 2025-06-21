from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from drf_spectacular.utils import extend_schema #type:ignore
from django.contrib.auth import get_user_model
from users.permissions import IsAuthenticated
from users.serializers.profile import ProfileSerializer

User = get_user_model()

@extend_schema(
    responses={200: ProfileSerializer},
)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
