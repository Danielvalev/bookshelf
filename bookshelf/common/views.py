from django.shortcuts import render
from books.models import Book


# Create your views here.


def landing_page(request):
    context = {
        'books': Book.objects.all().order_by('-id')[:10]  # .order_by('-id') - newest are on top
    }
    return render(request, 'landing_page.html', context)
