# Generated by Django 3.1.1 on 2020-09-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200926_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='second_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]