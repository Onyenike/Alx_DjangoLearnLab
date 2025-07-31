import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

# Example usage:
if name == 'main':
    # Create sample data
    author1 = Author.objects.create(name='Author 1')
    book1 = Book.objects.create(title='Book 1', author=author1)
    book2 = Book.objects.create(title='Book 2', author=author1)

    library1 = Library.objects.create(name='Library 1')
    library1.books.add(book1, book2)

    librarian1 = Librarian.objects.create(name='Librarian 1', library=library1)

    # Run queries
    books_by_author = query_books_by_author('Author 1')
    print("Books by Author 1:")
    for book in books_by_author:
        print(book.title)

    books_in_library = list_books_in_library('Library 1')
    print("\nBooks in Library 1:")
    for book in books_in_library:
        print(book.title)

    librarian = retrieve_librarian_for_library('Library 1')
    print("\nLibrarian for Library 1:")
    print(librarian.name)