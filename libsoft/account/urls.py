from django.urls import path
from .views import UserListView, UserCreateAPIView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view()),
    path('signup/', UserCreateAPIView.as_view()),
    path('<int:pk>/', UserDetailView.as_view())
]
