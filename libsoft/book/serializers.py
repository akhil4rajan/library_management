from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """
        Django Serializer to handle the CRUD operations of Book Details
    """

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        book = super(BookSerializer, self).create(validated_data)
        book.save()
        return book

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.author = validated_data.get('author', instance.author)
        instance.year_of_publication = validated_data.get('year_of_publication', instance.year_of_publication)
        instance.description = validated_data.get('description', instance.description)
        instance.availability = validated_data.get('availability', instance.availability)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance
