# Generated by Django 5.0 on 2023-12-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_reservation_day_reservation_targetday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='day',
        ),
        migrations.AddField(
            model_name='book',
            name='code',
            field=models.IntegerField(default=0),
        ),
    ]
