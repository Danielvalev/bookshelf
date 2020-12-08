from django.shortcuts import render
from django.views.generic.base import View

from books.models import Book


# Create your views here.


def landing_page(request):
    context = {
        'books': Book.objects.all().order_by('-id')[:10]  # .order_by('-id') - newest are on top
    }
    return render(request, 'landing_page.html', context)


class NoAccessView(View):
    def get(self, request):
        return render(request, 'no_permission.html')
