from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from rest_framework.throttling import UserRateThrottle #type:ignore
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.serializers.password_reset import PasswordResetRequestSerializer
from users.utils import send_password_reset_email 

User = get_user_model()

class PasswordResetRequestThrottle(UserRateThrottle):
    scope = 'password_reset'

class PasswordResetRequestView(APIView):
    throttle_classes = [PasswordResetRequestThrottle]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            send_password_reset_email(user, uid, token)

        except User.DoesNotExist:
           pass

        
        
        return Response(
            {'detail': 'If the email exists, a password reset link has been sent.'},
            status=status.HTTP_200_OK
        )