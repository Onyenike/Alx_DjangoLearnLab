from django.urls import path, include
from .views import BookList


urlpatterns = [
    path("api/books", BookListCreateAPIView.as_view(), name="book_list_create")
]

