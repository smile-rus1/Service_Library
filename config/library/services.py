import datetime

from django.shortcuts import get_object_or_404

from .models import Reader, Book, BookLoan


def get_reader_id(reader_id: int) -> Reader:
    """
    возвращает reader по id
    """
    reader = Reader.objects.get(id=reader_id)
    return reader


def get_reader(surname: str) -> Reader | bool:
    """
    возвращает Reader по surname
    """
    reader = Reader.objects.get(surname=surname)
    return reader


def get_reader_by_surname() -> list[str]:
    """
    возвращает list с surname читателей
    """
    surnames = Reader.objects.values_list("surname", flat=True)
    return list(surnames)


def register_reader(reader_data: dict) -> bool:
    """
    функция записывающего читателя данные
    """
    if _exists_reader(reader_data["surname"]):
        return False

    reader, created = Reader.objects.get_or_create(
        name=reader_data["name"],
        surname=reader_data["surname"],
        last_name=reader_data["last_name"]
    )
    if not created:
        return False

    return True


def _exists_reader(surname: str) -> bool:
    """
    проверяет существует ли читатель
    """
    try:
        reader_exists = get_object_or_404(Reader, surname=surname)
        if reader_exists:
            return True
    except:
        return False


def get_is_available_book():
    """
    проверяет и возвращает все доступные книги
    """
    books = Book.objects.filter(bookstorage__is_available=True)
    return books


def _get_one_is_available_book(book_id: int):
    """
    проверят, является ли книга еще доступной
    """
    try:
        book = Book.objects.get(id=book_id)
        return book.bookstorage.is_available
    except Book.DoesNotExist:
        return False


def borrow_book(reader_id: int, book_id: int):
    """
    функция в которой читатель берет книгу
    """
    try:
        if not _get_one_is_available_book(book_id):
            return False

        reader = Reader.objects.get(id=reader_id)
        book = Book.objects.get(id=book_id)
        loan = BookLoan.objects.create(reader=reader, book=book, date_borrow=datetime.date.today())
        book.bookstorage.is_available = False
        book.bookstorage.save()
        return True
    except:
        return False


def reader_borrowed_books(reader_id: int):
    """
    возвращает все книги читателя, которые он взял
    """
    borrowed_books = BookLoan.objects.filter(reader=reader_id, date_return__isnull=True)
    return borrowed_books


def return_book(reader_id: int, book_id: int) -> bool:
    """
    функция для возврата книги от читателя
    """
    try:
        loan = BookLoan.objects.get(
            book__bookstorage__id=book_id,
            reader_id=reader_id,
            date_return__isnull=True
        )
        loan.book.bookstorage.is_available = True
        loan.book.bookstorage.save()
        loan.date_return = datetime.date.today()
        loan.save()
        return True

    except:
        return False
