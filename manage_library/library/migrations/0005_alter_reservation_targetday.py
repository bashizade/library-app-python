# Generated by Django 5.0 on 2023-12-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_reservation_targetday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='targetDay',
            field=models.CharField(max_length=255, null=True),
        ),
    ]