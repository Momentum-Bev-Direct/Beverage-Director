# Generated by Django 3.0.4 on 2020-03-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bevdir', '0009_merge_20200326_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='portion',
            name='price_per_unit',
            field=models.FloatField(default=0),
        ),
    ]
