from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework.exceptions import ValidationError, PermissionDenied #type:ignore
from rest_framework import status #type:ignore
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from users.permissions import IsAuthenticated

User = get_user_model()

class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        user = request.user
        action = request.data.get('action')

        target_user = user if pk is None else get_object_or_404(User, pk=pk)
       
        if target_user != user and not user.is_staff:
            raise PermissionDenied(
                'Only admins can manage other users.'
            )

        open_orders = target_user.orders.exclude(status='done')
        if action in ['delete', 'deactivate'] and open_orders.exists():
            raise ValidationError(
                'Action not allowed: user has open orders.'
            )

        if action == 'delete':
            target_user.delete()
            return Response({'detail' : 'User deleted.'}, status=status.HTTP_200_OK)
        
        elif action == 'deactivate':
            target_user.is_active = False
            target_user.deactivated_at = timezone.now()
            target_user.save()
            return Response(
                {
                    'detail' : 'User deactivated.',
                    'message' : 'You have 15 days to reactivate by logging in.'
                },
                status=status.HTTP_200_OK
            )
        
        elif action == 'activate':
            if not user.is_staff:
                raise PermissionDenied(
                    'Only admins can activate users.'
                )
            target_user.is_active = True
            target_user.deactivated_at = None
            target_user.save()
            return Response(
                {
                'detail' : 'User activated.'
                },
                status=status.HTTP_200_OK
            )
        
        raise ValidationError('Invalid action')