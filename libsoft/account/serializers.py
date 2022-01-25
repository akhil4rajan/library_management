from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """
    Django Serializer to handle the User Create operation
    """
    name = serializers.SerializerMethodField('get_user_full_name')

    def get_user_full_name(self, obj):
        return obj.get_full_name() if obj.get_full_name() else obj.username

    class Meta:
        model = User
        fields = ('id', 'name', 'first_name', 'last_name', 'username', 'email',
                  'last_login', 'is_superuser', 'is_active', 'is_staff', 'date_joined', 'password',
                  )

        read_only_fields = ('id', 'date_joined', 'last_login')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        if validated_data.get('email', None):
            user.email = validated_data.get('email', None)
        if validated_data.get('first_name', None):
            user.first_name = validated_data.get('first_name', None)
        if validated_data.get('last_name', None):
            user.last_name = validated_data.get('last_name', None)

        if validated_data.get('email', None) or validated_data.get('first_name', None) or validated_data.get(
                'last_name', None):
            user.save()
        return user
