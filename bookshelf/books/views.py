from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from books.forms import CreateBookForm

# Create your views here.
from books.models import Book


@login_required
def add_book(request):
    if request.method == 'GET':
        form = CreateBookForm()

        context = {
            'form': form,
        }

        return render(request, 'books/add_book.html', context)
    else:
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)  # Need to add commit=False for take the user
            book.user = request.user  # Add the user from request.user
            form.save()
            return redirect('index')

        context = {
            'form': form
        }

        return render(request, 'books/add_book.html', context)
