from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import UserProfile
from  articles.serializers import PostedArticlesSerializer


## UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    
   class Meta:
       model = UserProfile
       fields = "__all__"


## User Serializer
class UserSerializer(serializers.ModelSerializer):
   
    user_profile = UserProfileSerializer(source='userprofile', read_only= True)
    posted = PostedArticlesSerializer(source='articles', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'user_profile', 'posted')


## Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

    # def to_representation(self, instance):
    #     data = super(RegisterSerializer,self).to_representation(instance)
    #     profile = data.pop('profile')
    #     for key,val in profile.items():
    #         data.update({key:val})
    #     return data

## Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Creds. ")


## for login
class forLogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

