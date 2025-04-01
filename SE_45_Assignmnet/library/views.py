from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library Management System!")

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
