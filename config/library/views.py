from django.shortcuts import render, redirect

from . import services


def index(request):
    """
    Главная страница, на которой можно выбрать "регистрацию"|"авторизацию" читателя.
    """
    return render(request, "index.html")


def login_reader(request):
    """
    "Авторизация" читателя по surname.
    """
    surnames = services.get_reader_by_surname()

    if request.method == "POST":
        reader = services.get_reader(request.POST.get("selected_surname"))
        return redirect("home_reader", reader_id=reader.id)

    return render(request, "login.html", {"surnames": surnames})


def register_reader(request):
    """
    Регистрация читателя по name, surname, last_name.
    При чем, если пользователь с фамилией уже есть в списке, то придется использовать другую фамилию.
    """
    if request.method == "POST":
        if not services.register_reader(
                {
                    "name": request.POST.get("name"),
                    "surname": request.POST.get("surname"),
                    "last_name": request.POST.get("last_name")
                }
        ):
            return render(request, "register.html", {"message": "Такой читатель с такой фамилией уже в системе есть!"})

        return redirect("login")

    return render(request, "register.html")


def home_reader(request, reader_id: int):
    """
    Домашняя страница читателя.
    """
    reader = services.get_reader_id(reader_id)

    if not reader:
        return redirect("index")

    return render(
        request, "reader_home.html", {
            "reader": reader,
            "books": services.reader_borrowed_books(reader_id)
        }
    )


def is_available_book(request, reader_id):
    """
    Доступные книги читателям.
    Также пользователю может взять одну из доступных книг
    """
    if request.method == "POST":
        if services.borrow_book(
                reader_id,
                request.POST.get("book")
        ):
            return redirect("home_reader", reader_id=reader_id)
        else:
            return render(request, "available_book.html",
                          {
                              "message": "Книга не была взята, возможно ее уже взяли!",
                              "books": services.get_is_available_book()
                          }
                          )

    return render(request, "available_book.html", {"books": services.get_is_available_book()})


def return_book(request, reader_id: int):
    if request.method == "POST":
        if services.return_book(
            reader_id,
            request.POST.get("book")
        ):
            return redirect("home_reader", reader_id=reader_id)
        else:
            render(request, "return_book.html", {
                "message": "Возможно, уже уже вернули эту книгу, или ее не существует"
            }
                   )
    return render(request, "return_book.html")
