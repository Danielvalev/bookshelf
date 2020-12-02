from django.db import models
from django.db.models import PROTECT


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    # cover_type choices
    PAPERBACK = 'paperback'
    HARDCOVER_CASE_WRAP = 'hardcover case wrap'
    HARDCOVER_DUST_JACKET = 'hardcover dust jacket'

    COVER_TYPES = (
        (PAPERBACK, 'Paperback'),
        (HARDCOVER_CASE_WRAP, 'Hardcover Case Wrap'),
        (HARDCOVER_DUST_JACKET, 'Hardcover Dust Jacket'),
    )

    # condition choices
    NEW = 'new'
    LIKE_NEW = 'like new'
    USED = 'used'

    CONDITIONS = (
        (NEW, 'New'),
        (LIKE_NEW, 'Like New'),
        (USED, 'Used'),
    )

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    page_count = models.IntegerField()
    description = models.TextField(max_length=1000, default='')
    publisher = models.CharField(max_length=50, blank=True)
    cover_type = models.CharField(max_length=21, choices=COVER_TYPES, default=PAPERBACK)
    image = models.ImageField(upload_to='public/book_covers', blank=True, null=True)
    condition = models.CharField(max_length=10, choices=CONDITIONS, default=USED)
    category = models.ForeignKey(Category, on_delete=PROTECT)

    def __str__(self):
        return f'{self.author}, Title: {self.title}'
