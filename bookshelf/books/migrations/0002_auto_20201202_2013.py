# Generated by Django 3.1.2 on 2020-12-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]