from django.urls import path
from .views import TrackBookListView, TrackBookCreateAPIView, TrackBookDetailView, BookActionView

urlpatterns = [
    path('', TrackBookListView.as_view()),
    path('add/', TrackBookCreateAPIView.as_view()),
    path('<int:pk>/', TrackBookDetailView.as_view()),
    path('book_action/', BookActionView.as_view())

]
