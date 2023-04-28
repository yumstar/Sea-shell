from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import  Response
from .serializers import CenterUserSerializer, CenterUserRegisterSerializer, CenterUserSigninSerializer, TagSerializer, MessageSerializer, DayExperienceSerializer
from rest_framework import permissions, status, generics
from .validation import validate_user_data, validate_user_email, validate_user_password
from .models import Message, Tag, DayExperience
from .permissions import IsUser
# Create your views here.


class CenterUserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        validated_data = validate_user_data(request.data)
        serializer = CenterUserRegisterSerializer(data=validated_data)
        if serializer.is_valid(raise_exception=True):
            center_user = serializer.create(validated_data)
            if center_user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CenterUserSignin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        assert validate_user_email(request.data)
        assert validate_user_password(request.data)
        serializer = CenterUserSigninSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            authenticated_user = serializer.authenticate_user(request.data)
            login(request, authenticated_user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CenterUserSignout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class CenterUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = CenterUserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,IsUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,IsUser,)

class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,IsUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MessageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,IsUser,)

class DayExperienceListView(generics.ListCreateAPIView):
    queryset = DayExperience.objects.all()
    serializer_class = DayExperienceSerializer
    permission_classes = (permissions.IsAuthenticated, IsUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DayExperienceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DayExperience.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,IsUser,)