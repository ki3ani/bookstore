from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.comment

    class Meta:
        indexes = [
            models.Index(fields=['book']),
        ]

class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, through='AuthorBook'  , related_name='author_books')

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]


class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_name')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='author_book')

    def __str__(self):
        return f'{self.author} - {self.book}'


    class Meta:
        indexes = [
            models.Index(fields=['author']),
            models.Index(fields=['book']),
        ]







