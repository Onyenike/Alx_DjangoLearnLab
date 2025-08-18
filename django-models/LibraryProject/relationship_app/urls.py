from .views import list_books, LibraryDetailView
from django.urls import path
from . import views

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name="library_detail"),

