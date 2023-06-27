from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import  Response
from .serializers import CenterUserSerializer, CenterUserRegisterSerializer, CenterUserSigninSerializer, TagSerializer, MessageSerializer, DayExperienceSerializer
from rest_framework import permissions, status, generics
from .validation import validate_user_data, validate_user_email, validate_user_password, validate_tag_data, validate_message_data
from .models import Message, Tag, DayExperience, CenterUser
from .permissions import IsUser
from django.http import HttpResponse, JsonResponse
# Create your views here.
# import environ
# env = environ.Env()
# SECURE_COOKIE = env('BACKEND_STAGE')

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
            return Response({'message': 'Login sucessful.'}, status=status.HTTP_200_OK)


class CenterUserSignout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout sucessful.'}, status=status.HTTP_200_OK)


class CenterUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = CenterUserSerializer(request.user)
        res = Response({'user': serializer.data}, status=status.HTTP_200_OK)
        res.delete_cookie('sessionid')
        res.delete_cookie('csrftoken')
        return res


class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,IsUser,)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        if not hasattr(data, 'user'):
            data['user'] = self.request.user.center_user_id
        validated_data = validate_tag_data(data, self.request.user)
        serializer = TagSerializer(data=validated_data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response({'message':'Tag not able to be created.'},status=status.HTTP_400_BAD_REQUEST)

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

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        if not data.get('user'):
            data['user'] = self.request.user.center_user_id
        if data.get('tags') is not None and isinstance(data['tags'], list):
            for tag in data['tags']:
                tag['user'] = self.request.user.center_user_id
        validated_data = validate_message_data(data, self.request.user)
        serializer = MessageSerializer(data=validated_data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(status=status.HTTP_201_CREATED)
        return Response({'message':'Message not able to be created.'},status=status.HTTP_400_BAD_REQUEST)
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