# Generated by Django 3.0.4 on 2020-03-25 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bevdir', '0005_auto_20200325_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='misc',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='spirits',
        ),
    ]
