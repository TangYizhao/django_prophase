# Generated by Django 2.2.12 on 2021-01-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.CharField(default='', max_length=50, verbose_name='描述'),
        ),
    ]
