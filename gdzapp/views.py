from .serializers import *
from rest_framework import generics
from . import models
from parser import parse_data
from rest_framework.response import Response


class BookAPIView(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer


class BookAddRequestView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        parse_data(models)

        books = models.Book.objects.all()
        return Response(data=BookSerializer(books, many=True).data)
