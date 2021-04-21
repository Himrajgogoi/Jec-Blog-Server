from rest_framework import generics, permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, UserProfileSerializer, forLogin
from .models import UserProfile


##RegisterAPI
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context= self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


## LoginAPI
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        return Response({
            'user': forLogin(user, context = self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        })


## UserAPI for all users
class UserAPI(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


## User Api for personal
class PersonalUser(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self):
        return self.request.user

##ProfileUpdate
class Profile(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = UserProfile.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)