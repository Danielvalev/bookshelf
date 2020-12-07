from django import forms
from books.models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)

