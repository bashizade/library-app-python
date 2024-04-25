from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=11)
    nationalCode = models.CharField(max_length=10)


class Book(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(default=0)
    status = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=255)


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    targetDay = models.CharField(max_length=255, null=True)
    info = models.CharField(max_length=255, default=" ")
