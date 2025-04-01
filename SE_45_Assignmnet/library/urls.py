from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    # Book Endpoints
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
