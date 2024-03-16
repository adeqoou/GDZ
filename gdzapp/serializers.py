from rest_framework import serializers
from .models import *


class CoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cover
        fields = ('id', 'url')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'title')


class TaskImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskImage
        fields = ('id', 'url')


class TaskSerializers(serializers.ModelSerializer):
    images = TaskImageSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'images')


class PartsSerializers(serializers.ModelSerializer):
    tasks = TaskSerializers(many=True)

    class Meta:
        model = Parts
        fields = ('id', 'title', 'tasks')


class BookSerializer(serializers.ModelSerializer):
    cover = CoverSerializer()
    subject = SubjectSerializer()
    parts = PartsSerializers(many=True)

    class Meta:
        model = Book
        fields = '__all__'








