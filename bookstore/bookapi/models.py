from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_year = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=255, default='No genre specified')
    isbn = models.CharField(max_length=13, default='No ISBN specified')
    description = models.TextField(default='No description available')
    cover = models.ImageField(upload_to='covers', blank=True, null=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    website = models.URLField()

class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    text = models.TextField()
    reviewer = models.CharField(max_length=255)
    rating = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    purchase_history = models.ManyToManyField(Book)
