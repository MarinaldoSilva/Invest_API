from .models import User
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class UserListMyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request:Request) -> Response:
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request:Request) -> Response:
        user = request.user
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)