from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(read_only=True, source='followers.count')
    following_count = serializers.IntegerField(read_only=True, source='following.count')

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','bio','profile_picture','followers_count','following_count']
        read_only_fields = ['id','followers_count','following_count']

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def validate_password(self, value):
        validate_password(value)
        return value
    class Meta:
        model = User
        fields = ['username','email','password']
    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data.get('email',''))
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        data['user'] = user
        return data
