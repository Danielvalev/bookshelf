from django.contrib import admin
from books.models import Book, Category

# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
