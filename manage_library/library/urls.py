from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users', views.Users, name="users"),
    path('books', views.Books, name="books"),
    path('reservations', views.Reservations, name="reservations"),
    path('categories', views.Categories, name="categories"),
    path('create/category', views.createCategory, name="createCategory"),
    path('create/user', views.createUser, name="createUser"),
    path('create/book', views.createBook, name="createBook"),
    path('delete/book/<int:book_id>', views.deleteBook, name="deleteBook"),
    path('create/reservation', views.createReservation, name="createReservation"),
    path('delete/reservation/<int:reservation_id>', views.deleteReservation, name="deleteReservation"),
    path('user/card', views.UserCard, name="userCard")

]
