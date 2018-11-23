from django.contrib.auth import get_user_model, authenticate
from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

from openbook_common.responses import ApiMessageResponse
from .serializers import RegisterSerializer, UsernameCheckSerializer, EmailCheckSerializer, LoginSerializer, \
    GetAuthenticatedUserSerializer, GetUserSerializer, UpdateAuthenticatedUserSerializer
from .models import UserProfile


class Register(APIView):
    """
    The API to register a new user
    """
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(serializer.validated_data)

    def on_valid_request_data(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        birth_date = data.get('birth_date')
        name = data.get('name')
        avatar = data.get('avatar')
        User = get_user_model()

        with transaction.atomic():
            new_user = User.objects.create_user(email=email, username=username, password=password)
            UserProfile.objects.create(name=name, user=new_user, birth_date=birth_date, avatar=avatar)

        user_auth_token = new_user.auth_token

        return Response({
            'token': user_auth_token.key
        }, status=status.HTTP_201_CREATED)


class UsernameCheck(APIView):
    """
    The API to check if a username is both valid and not taken.
    """
    serializer_class = UsernameCheckSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # The serializer contains the username checks, meaning at this line, it's all good.
        return ApiMessageResponse(_('Username available'), status=status.HTTP_202_ACCEPTED)


class EmailCheck(APIView):
    """
    The API to check if a email is both valid and not taken.
    """
    serializer_class = EmailCheckSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # The serializer contains the email checks, meaning at this line, it's all good.
        return ApiMessageResponse(_('Email available'), status=status.HTTP_202_ACCEPTED)


class Login(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(serializer.validated_data)

    def on_valid_request_data(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            raise AuthenticationFailed()


class AuthenticatedUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_serializer = GetAuthenticatedUserSerializer(request.user, context={"request": request})
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer = UpdateAuthenticatedUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = request.user

        with transaction.atomic():
            user.update(**data)

        user_serializer = GetAuthenticatedUserSerializer(user, context={"request": request})
        return Response(user_serializer.data, status=status.HTTP_200_OK)


class User(APIView):
    def get(self, request, user_uuid):
        user = request.user.get_user_with_uuid(user_uuid)
        user_serializer = GetUserSerializer(user, context={"request": request})
        return Response(user_serializer.data, status=status.HTTP_200_OK)
