# Generated by Django 3.1.1 on 2020-09-06 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_movie_director'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('title', 'released')},
        ),
    ]
