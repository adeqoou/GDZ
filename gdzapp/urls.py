from django.urls import path
from . import views

urlpatterns = [
    path('api/book/', views.BookAPIView.as_view(), name='book_api'),
    path('api/book/fill/', views.BookAddRequestView.as_view(), name='book_api_fill'),
    path('api/book/fetch-image/', views.GetBookImage.as_view(), name='ferjgio')
]