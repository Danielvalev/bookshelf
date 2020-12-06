from django.urls import path

from books.views import add_book

urlpatterns = [
    path('add/', add_book, name='add book'),

]