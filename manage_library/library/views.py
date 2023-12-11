from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from . import forms
from . import models


# Create your views here.
def index(request):
    return render(request, 'index.html')


def Users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def Books(request):
    books = models.Book.objects.all()
    return render(request, 'books.html', {'books': books})


def Reservations(request):
    reservations = models.Reservation.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations})


@require_POST
def createUser(request):
    form = forms.CreateUserForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = User(username=data["username"],
                    first_name=data["firstname"],
                    last_name=data['lastname'],
                    email=data['email'],
                    password=data['password']
                    ).save()
        models.Profile(user=user,
                       phone=data['phone'],
                       nationalCode=data['nationalCode']).save()
        messages.success(request, 'کاربر با موفقیت ساخته شد')
        return redirect('users')
    else:
        messages.error(request, 'خطا در ساخت کاربر')
        return redirect('users')


@require_POST
def createBook(request):
    form = forms.createBook(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        models.Book(name=data['name']).save()
        messages.success(request, 'کتاب مورد نظر با موفقیت ثبت شد')
        return redirect('books')
    else:
        messages.success(request, 'خطا در ثبت کتاب مورد نظر')
        return redirect('books')


def deleteBook(request, book_id):
    models.Book.objects.get(id=book_id).delete()
    messages.success(request, 'کتاب مورد نظر با موفقیت حذف شد')
    return redirect('books')


@require_POST
def createReservation(request):
    form = forms.createReservation(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        models.Reservation(user_id=data['user_id'],
                           book_id=data['book_id'],
                           day=data['day'],
                           targetDay=data['targetDay']
                           ).save()
        messages.success(request, 'رزرو مورد نظر با موفقیت ثبت شد')
        return redirect('reservations')
    else:
        messages.success(request, 'خطا در ثبت رزرو مورد نظر')
        return redirect('reservations')


def deleteReservation(request, reservation_id):
    models.Reservation.objects.get(id=reservation_id).delete()
    messages.success(request, 'رزرو مورد نظر با موفقیت حذف شد')
    return redirect('reservations')
