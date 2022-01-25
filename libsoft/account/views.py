from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from .models import User
from . import serializers


class UserListView(generics.ListAPIView):
    """
    Django API to return the List of Users
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return []


class UserCreateAPIView(generics.CreateAPIView):
    """
    Django API to create Users
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Django API to return the Details of the User
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
