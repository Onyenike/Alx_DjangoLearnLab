
from django.urls import path
from . import views

urlpatterns = [
    path('DetailView/', views.library_detail),
    path('book_list/', views.list_books),
]