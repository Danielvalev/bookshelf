from django.urls import path

from books.views import add_book, details_book, edit_book, delete_book, BooksListView

urlpatterns = [
    path('add/', add_book, name='add book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('list', BooksListView.as_view(), name='list books'),  # Inherit from ListView

]
