from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from users.serializers.password_reset import PasswordResetConfirmSerializer

User = get_user_model()

class PasswordResetConfirmView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            uid = urlsafe_base64_decode(serializer.validated_data['uidb64']).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError, UnicodeDecodeError):
            return Response(
                {'detail': 'Invalid user'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not default_token_generator.check_token(user, serializer.validated_data['token']):
            return Response(
                {'detail': 'Invalid or expired token'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(serializer.validated_data['new_password'])
        user.save()

        return Response(
            {'detail': 'Password reset successful'}, 
            status=status.HTTP_200_OK
        )