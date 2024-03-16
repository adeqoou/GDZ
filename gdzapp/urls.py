from django.urls import path
from . import views

urlpatterns = [
    path('api/book/', views.BookAPIView.as_view(), name='book_api'),
]