from django.contrib import admin
from .models import Book, Review, Author, AuthorBook

#Register your models here.


admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Author)
admin.site.register(AuthorBook)


