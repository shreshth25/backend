from rest_framework import serializers
from . models import User, Post, Reel
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email']

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            data['image'] = settings.BASE_URL + instance.image.url
        return data
    

class ReelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Reel
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.video:
            data['video'] = settings.BASE_URL + instance.video.url
        return data
