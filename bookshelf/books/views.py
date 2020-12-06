from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from books.forms import BookForm


# Create your views here.
from books.models import Book


@login_required
def add_book(request):
    if request.method == 'GET':
        form = BookForm()

        context = {
            'form': form,
        }

        return render(request, 'books/add_book.html', context)
    else:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            book = Book(user=form.cleaned_data['user'])
            print(book)
            book.user = request.user
            print(f'this is book.user: {book.user}, and this is {book.user_id}')
            form.save()
            return redirect('index')

        context = {
            'form': form
        }

        return render(request, 'books/add_book.html', context)
