from django.shortcuts import render
from . models import Book 
from  . models import Library
# Create your views here.
def library_detail(request):
    tours = Library.objects.all()
    context = {'tours':tours}
    return render(request, "relationship_app/library_books.html")

def list_books(request):
    books = Book.objects.all()
    context = {'book':books}
    return render(request, "relationship_app/list_books.html")



