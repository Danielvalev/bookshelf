from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from books.models import Book

from books.forms import CreateBookForm


# Create your views here.


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


@login_required
def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'book': book,
            'can_delete': request.user == book.user,
            'can_edit': request.user == book.user,
        }

        return render(request, 'books/book_detail.html', context)
    else:
        pass


@login_required
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if book.user != request.user:
        # Cannot do it
        # raise Exception('You have no permission to edit that book, because you are not the owner!')
        return render(request, 'no_permission.html')
    if request.method == 'GET':
        form = CreateBookForm(instance=book)

        context = {
            'form': form,
            'book': book,
        }

        return render(request, 'books/book_edit.html', context)
    else:
        form = CreateBookForm(
            request.POST,
            instance=book
        )
        if form.is_valid():
            form.save()
            return redirect('details book', book.pk)

        context = {
            'form': form,
            'book': book,
        }
        return render(request, 'books/book_edit.html', context)


@login_required
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if book.user != request.user:
        # Cannot do it
        # raise Exception('You have no permission to delete that book, because you are not the owner!')
        return render(request, 'no_permission.html')
    if request.method == 'GET':
        context = {
            'book': book,
        }
        return render(request, 'books/book_delete.html', context)

    else:
        book.delete()
        return redirect('index')


# CBV
class BooksListView(ListView):
    template_name = 'books/list_books.html'
    model = Book
    context_object_name = 'books'  # Default is object
    paginate_by = 10
