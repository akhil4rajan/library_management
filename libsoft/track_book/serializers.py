from rest_framework import serializers

from .models import TrackBook
from account.serializers import UserSerializer
from book.serializers import BookSerializer


class TrackBookSerializer(serializers.ModelSerializer):
    """
        Django Serializer to handle the Recommendation Engines CRUD operations
    """
    user_info = UserSerializer(source='Algo', read_only=True)
    book_info = BookSerializer(source='Book', read_only=True)

    class Meta:
        model = TrackBook
        fields = ('user_info', 'book_info', 'status')

        # fields = '__all__'

    def create(self, validated_data):
        track_book = super(TrackBookSerializer, self).create(validated_data)
        track_book.save()
        return track_book

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.book_id = validated_data.get('book_id', instance.book_id)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance
