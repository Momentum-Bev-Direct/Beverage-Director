# Generated by Django 3.0.4 on 2020-03-24 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bevdir', '0004_portion_shot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscingredient',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
