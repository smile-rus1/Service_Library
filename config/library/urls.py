from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_reader, name="login"),
    path("register/", views.register_reader, name="register"),
    path("home_reader/<int:reader_id>", views.home_reader, name="home_reader"),
    path("available_book/<int:reader_id>", views.is_available_book, name="available_book"),
    path("return_book/<int:reader_id>", views.return_book, name="return_book")
]
