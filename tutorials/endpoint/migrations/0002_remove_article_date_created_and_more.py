# Generated by Django 4.0.3 on 2022-03-14 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_updated',
        ),
    ]
