from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .sendmails import book_alert_mail
from .models import TrackBook
from . import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q

class TrackBookListView(generics.ListAPIView):
    """
    Django API to return the List of Book
    """
    queryset = TrackBook.objects.all()
    serializer_class = serializers.TrackBookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return TrackBook.objects.all()
        return []


class TrackBookCreateAPIView(generics.CreateAPIView):
    """
    Django API to create Book Data
    """
    queryset = TrackBook.objects.all()
    serializer_class = serializers.TrackBookSerializer
    permission_classes = (AllowAny,)


class TrackBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Django API to return the Details of the Book
    """
    queryset = TrackBook.objects.all()
    serializer_class = serializers.TrackBookSerializer


class BookActionView(APIView):
    """
        Django API to calculate total books in the Library
    """

    def post(self, request):
        book_id = request.data.get('book')
        user_id = request.data.get('user')
        user_action = request.data.get('action')

        if book_id is not None and user_id is not None:
            track_data = TrackBook.objects.filter(book_id=book_id, user_id=user_id).first()
            if user_action:
                track_data.status = True
                info_text = "user have returned the book"

            else:
                track_data.status = False
                info_text = "user have borrowed the book"

            track_data.save()
            status_code = status.HTTP_200_OK
            # Sending the Email Notifications
            user_data = User.objects.filter(name=user_id)
            book_alert_mail(user_data['email'])
        else:
            info_text = "Input book_id or user_id is invalid"
            status_code = status.HTTP_400_BAD_REQUEST

        api_response = {
            "command": "book_action",
            "info": info_text
        }
        return Response(api_response, status=status_code)
