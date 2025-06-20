from rest_framework import generics #type:ignore
from django.contrib.auth import get_user_model
from users.permissions import IsAuthenticated, IsAdmin
from users.serializers import ProfileUpdateSerializer

User = get_user_model()

class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class AdminProfileUpdateView(generics.UpdateAPIView):
    throttle_classes = []
    queryset = User.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'pk'