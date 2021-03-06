# Generated by Django 3.1.2 on 2020-12-02 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=50)),
                ('page_count', models.IntegerField()),
                ('description', models.TextField(default='', max_length=500)),
                ('publisher', models.CharField(blank=True, max_length=50)),
                ('cover_type', models.CharField(choices=[('paperback', 'Paperback'), ('hardcover case wrap', 'Hardcover Case Wrap'), ('hardcover dust jacket', 'Hardcover Dust Jacket')], default='paperback', max_length=21)),
                ('image', models.ImageField(blank=True, null=True, upload_to='public/book_covers')),
                ('condition', models.CharField(choices=[('new', 'New'), ('like new', 'Like New'), ('used', 'Used')], default='used', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.category')),
            ],
        ),
    ]
