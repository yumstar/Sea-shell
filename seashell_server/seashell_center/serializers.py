from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import ValidationError
from .models import Message, Tag, DayExperience

UserModel = get_user_model()


class CenterUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, validated_data):
        user = UserModel.objects.create_user(email=validated_data['email'], password=validated_data['password'])
        user.name = validated_data['name']
        user.save()
        return user
class CenterUserSigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def authenticate_user(self, user_data):
        user = authenticate(username=user_data['email'], password=user_data['password'])
        if not user:
            raise ValidationError('User with given credentials does not exist.')
        return user
class CenterUserSerializer(serializers.ModelSerializer):
    messages = serializers.PrimaryKeyRelatedField(many=True, queryset=Message.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    # tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='text')
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserModel
        fields = ('email', 'name', 'messages', 'tags', 'user')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'user', 'text', 'color']


class MessageSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Message
        fields = ['id', 'user', 'body', 'created', 'tags']
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        message_user = validated_data['user']
        message = Message.objects.create(**validated_data)
        for tag_data in tags_data:
            tag_obj, created = Tag.objects.get_or_create(text=tag_data['text'], user=message_user, defaults={'color': 'black'})
            message.tags.add(tag_obj)
        return message



class DayExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayExperience
        fields = ['id', 'user', 'date', 'experience']