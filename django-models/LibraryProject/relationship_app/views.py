from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def library_detail(request):
    return render(request, 'library_detail.html')

def list_books(request):
    return render(request, 'list_books.html')

