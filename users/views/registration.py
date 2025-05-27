from rest_framework import status #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework.response import Response #type:ignore
from users.serializers.registration import RegistrationSerializer

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Registration was successful'},
                            status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)