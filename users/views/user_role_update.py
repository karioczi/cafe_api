from rest_framework import generics, serializers #type:ignore
from rest_framework.exceptions import PermissionDenied #type:ignore
from django.contrib.auth import get_user_model
from users.serializers import UserRoleUpdateSerializer
from users.permissions import IsAdmin

User = get_user_model()

class UserRoleUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleUpdateSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'pk'

    def perform_update(self, serializer):
        if self.request.user.pk == self.get_object().pk:
            raise PermissionDenied(
                'You cant change your own role'
            )
        serializer.save()