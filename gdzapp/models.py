from django.db import models
from django.contrib.postgres.fields import ArrayField


class Cover(models.Model):
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.url


class Subject(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class TaskImage(models.Model):
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.url


class Task(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    images = models.ManyToManyField(to=TaskImage)

    def __str__(self):
        return self.title


class Parts(models.Model):
    title = models.PositiveIntegerField(default=1)
    tasks = models.ManyToManyField(to=Task)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField()
    classes = ArrayField(
        models.IntegerField()
    )
    authors = ArrayField(
        models.CharField(max_length=255)
    )
    description = models.TextField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    subtype = models.CharField(max_length=255, null=True, blank=True)
    parts = models.ManyToManyField(to=Parts)
    search_keywords = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    cover = models.ForeignKey(to=Cover, on_delete=models.CASCADE)








