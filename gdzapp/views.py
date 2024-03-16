from .serializers import *
from rest_framework import generics
from . import models
from .parser import parse_data
from rest_framework.response import Response
from django.shortcuts import render


class BookAPIView(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer

#
# def request_db(request):
#     my_data = Cover.objects.all()
#     return render('gdzapp/api1.html', {})


class BookAddRequestView(generics.RetrieveAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        parse_data(models)

        books = models.Book.objects.all()
        return books
