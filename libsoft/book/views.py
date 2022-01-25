from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q

from .models import Book
from . import serializers


class BookListView(generics.ListAPIView):
    """
    Django API to return the List of Book
    """
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'Rose')
        order = self.request.GET.get('orderby', 'year_of_publication')
        new_context = Book.objects.filter(
            Q(name=filter_val) | Q(author=filter_val) | Q(year_of_publication=filter)
        ).order_by(order)
        return new_context


class BookCreateAPIView(generics.CreateAPIView):
    """
    Django API to create Book Data
    """
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (AllowAny,)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Django API to return the Details of the Book
    """
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer



class TotalBookView(APIView):
    """
        Django API to calculate total books in the Library
    """

    def post(self, request):
        try:
            queryset = Book.objects.filter(availability=True)
            print(queryset)
            book_data = queryset.values()
            if book_data:
                total_books = len(book_data)
            else:
                total_books = 0
            api_response = {
                "command": "total_books",
                "total_count": total_books,
            }
            status_code = status.HTTP_200_OK
        except RuntimeError as e:
            api_response = {}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(api_response, status=status_code)

