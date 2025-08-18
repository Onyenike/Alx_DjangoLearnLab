from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
def library_detail(request):
    return render(request, "relationship_app/library_detail.html"),

def list_books(request):
    return render(request, "relationship_app/list_books.html", "Book.objects.all()")





