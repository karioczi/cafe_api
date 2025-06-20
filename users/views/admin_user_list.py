from rest_framework import generics, filters #type:ignore
from django_filters.rest_framework import DjangoFilterBackend #type:ignore
from django.contrib.auth import get_user_model
from users.serializers import UserListSerializer
from users.permissions import IsAdmin

User = get_user_model()

class AdminUserListView(generics.ListAPIView):
    throttle_classes = []
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdmin]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['role', 'id']
    search_fields = ['email', 'username']