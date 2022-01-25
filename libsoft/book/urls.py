from django.urls import path
from .views import BookListView, BookCreateAPIView, BookDetailView, TotalBookView

urlpatterns = [
    path('', BookListView.as_view()),
    path('add/', BookCreateAPIView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
    path('total_books/', TotalBookView.as_view())
]
