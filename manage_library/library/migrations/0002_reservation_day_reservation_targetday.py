# Generated by Django 5.0 on 2023-12-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='day',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='targetDay',
            field=models.DateTimeField(null=True),
        ),
    ]
