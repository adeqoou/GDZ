from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.response import Response


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

