from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from users.serializers.password_reset import PasswordResetRequestSerializer

User = get_user_model()

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'detail':'User not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        return Response(
            {'uid': uid, 'token': token},
            status=status.HTTP_200_OK
        )