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
    categories = models.Category.objects.all()
    return render(request, 'books.html', {'books': books, 'categories': categories})

def Categories(request):
    categories = models.Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def UserCard(request):
    users = User.objects.all()
    return render(request, 'userCard.html', {'users': users})

def Reservations(request, form=None):
    if form is None:
        form = {}
    reservations = models.Reservation.objects.all()
    books = models.Book.objects.all()
    users = User.objects.all()
    return render(request, 'reservations.html', {'reservations': reservations, 'books': books, 'users': users, 'form':form})


@require_POST
def createUser(request):
    form = forms.CreateUserForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        User.objects.create(username=data["username"],
                            first_name=data["firstname"],
                            last_name=data['lastname'],
                            email=data['email'],
                            password=data['password']
                            ).save()
        user = User.objects.get(username=data['username'])
        models.Profile.objects.create(user=user,
                                      phone=data['phone'],
                                      nationalCode=data['nationalCode']).save()
        messages.success(request, 'کاربر با موفقیت ساخته شد')
        return redirect('users')
    else:
        messages.error(request, form.errors)
        return redirect('users')


@require_POST
def createBook(request):
    form = forms.createBook(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        models.Book(name=data['name'], code=data['code']).save()
        book = models.Book.objects.get(code=data['code'])

        for category in request.POST.getlist('categories'):
            models.BookCategory(book=book, category_id=category).save()

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
def createCategory(request):
    form = forms.createCategory(request.POST)
    print(form)
    if form.is_valid():
        data = form.cleaned_data
        models.Category(name=data['name']).save()
        messages.success(request, 'دسته بندی مورد نظر با موفقیت ثبت شد')
        return redirect('categories')
    else:
        messages.success(request, 'خطا در ثبت دسته بندی مورد نظر')
        return redirect('categories')

@require_POST
def createReservation(request):
    userCheck = models.Reservation.objects.filter(user_id=request.POST['user_id']).count()
    bookCheck = models.Reservation.objects.filter(book_id=request.POST['book_id']).count()
    print(request.POST)
    if bookCheck == 0:
        if userCheck < 4:
            form = forms.createReservation(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                models.Reservation(user_id=data['user_id'],
                                   book_id=data['book_id'],
                                   targetDay=data['targetDay'],
                                   info=data['info']
                                   ).save()
                messages.success(request, 'رزرو مورد نظر با موفقیت ثبت شد')
                return redirect('reservations')

            else:
                messages.error(request, 'خطا در ثبت رزرو مورد نظر')
                return redirect('reservations')
        else:
            messages.error(request, 'کاربر انتخابی 3 کتاب را به امانت دارد و نمی تواند کتاب جدیدی را به امانت بگیرد')
            return redirect('reservations')
    else:
        messages.error(request, 'کتاب انتخابی از قبل به امانت گرفته شده است')
        return redirect('reservations')



def deleteReservation(request, reservation_id):
    models.Reservation.objects.get(id=reservation_id).delete()
    messages.success(request, 'رزرو مورد نظر با موفقیت حذف شد')
    return redirect('reservations')
