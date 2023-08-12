from django.contrib import admin

from . import models

admin.site.register(models.Reader)
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.BookLoan)
admin.site.register(models.BookStorage)
