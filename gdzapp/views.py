from . import serializers
from rest_framework import generics
from . import models
from .parser import parse_data
from rest_framework.response import Response
from django.shortcuts import render
import base64
import requests


class BookAPIView(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

#
# def request_db(request):
#     my_data = Cover.objects.all()
#     return render('gdzapp/api1.html', {})


class BookAddRequestView(generics.RetrieveAPIView):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        parse_data(models)

        books = models.Book.objects.all()
        return books


class GetBookImage(generics.RetrieveAPIView):
    serializer_class = serializers.BookUrlSerializer

    def get(self, request, *args, **kwargs):
        data: serializers.BookUrlSerializer = self.get_serializer(*args, **kwargs).data
        return Response(data={'image': base64.b64encode(requests.get(data.image_url).content)})

