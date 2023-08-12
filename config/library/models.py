from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title}"


class Reader(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f"{self.surname} {self.name}"


class BookLoan(models.Model):
    date_borrow = models.DateField()
    date_return = models.DateField(null=True, blank=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Учет выдачи книги"
        verbose_name_plural = "Учет выдачи книг"

    def __str__(self):
        return f"{self.book.title}"


class BookStorage(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Учет хранения книги"
        verbose_name_plural = "Учет хранения книг"

    def __str__(self):
        return f"{self.book}"

