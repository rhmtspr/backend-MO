from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    '''
    Serializer class to serializer CustomUser model.
    '''

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

class UserRegisterationSerializer(serializers.ModelSerializer):
    '''
    Serializer class to serialize registration requests and create a new user.
    '''

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class UserLoginSerializer(serializers.Serializer):
    '''
    Serializer class to authenticate users with email and password
    '''

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')
    