from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/users', views.Users, name="users"),
    path('/books', views.Books, name="books"),
    path('/reservations', views.Reservations, name="reservations"),
    path('/create/user', views.createUser, name="createUser"),
    path('/create/book', views.createBook, name="createBook"),
    path('/delete/book/<int:book_id>', views.deleteBook, name="deleteBook"),
    path('create/reservation', views.createReservation, name="createReservation"),
    path('/delete/reservation/<int:reservation_id>', views.deleteReservation, name="deleteReservation")

]
