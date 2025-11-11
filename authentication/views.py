from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .utils import (
    DETAIL, 
    EMAIL_NOT_FOUND, 
    INVALID_CREDENCIAL,
    NOT_TOKEN_REFRESH, 
    ERROR_TOKEN
    )

from accounts.models import User
from accounts.serializer import UserSerializer


class SingupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        

        return Response(
            {"username": user.username,"email": user.email}
        )


class SinginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request) -> Response:
        email = request.data.get('email')
        password = request.data.get('password')

        user = get_object_or_404(User, email=email)

        if user.check_password(password):
            refresh_token = TokenObtainPairSerializer.get_token(user)
            access_token = refresh_token.access_token

            return Response({
                "access": str(access_token),
                "refresh": str(refresh_token)
            },status=status.HTTP_200_OK)
        return Response({
            DETAIL:INVALID_CREDENCIAL}, status=status.HTTP_401_UNAUTHORIZED)
    

class SignoutView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request)->Response:  
        token_refresh = request.data.get("refresh")
        user = request.user

        if not token_refresh:
            return Response(
                {DETAIL:NOT_TOKEN_REFRESH},
                status=status.HTTP_404_NOT_FOUND)
        try:
            token = RefreshToken(token_refresh)
            token.blacklist()
        except TokenError:
            raise AuthenticationFailed({DETAIL:ERROR_TOKEN}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_205_RESET_CONTENT)
