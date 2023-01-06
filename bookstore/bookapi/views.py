from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book, Review, Author
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books_json = [model_to_dict(book) for book in books]
        return JsonResponse(books_json, safe=False)
    elif request.method == 'POST':
        data = request.POST
        try:
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                price=data['price'],
            )
        except IntegrityError:
            return HttpResponse(status=400, reason='Bad Request', content='Book already exists')
        return JsonResponse(model_to_dict(book), status=201)


@csrf_exempt
def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponse(status=404, reason='Not Found', content='Book does not exist')
    if request.method == 'GET':
        return JsonResponse(model_to_dict(book))
    elif request.method == 'PUT':
        data = request.POST
        book.title = data['title']
        book.author = data['author']
        book.price = data['price']
        book.save()
        return JsonResponse(model_to_dict(book))
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)


@csrf_exempt
def review_list(request, book_id):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)
        reviews = book.review_set.all()
        reviews_json = [model_to_dict(review) for review in reviews]
        return JsonResponse(reviews_json, safe=False)
    elif request.method == 'POST':
        data = request.POST
        book = Book.objects.get(pk=book_id)
        review = book.review_set.create(
            reviewer=data['reviewer'],
            comment=data['comment'],
        )
        return JsonResponse(model_to_dict(review), status=201)


@csrf_exempt
def review_detail(request, book_id, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        return HttpResponse(status=404, reason='Not Found', content='Review does not exist')
    if request.method == 'GET':
        return JsonResponse(model_to_dict(review))
    elif request.method == 'PUT':
        data = request.POST
        review.reviewer = data['reviewer']
        review.comment = data['comment']
        review.save()
        return JsonResponse(model_to_dict(review))
    elif request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=204)

@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        authors_json = [model_to_dict(author) for author in authors]
        return JsonResponse(authors_json, safe=False)
    elif request.method == 'POST':
        data = request.POST
        try:
            author = Author.objects.create(
                name=data['name'],
            )
        except IntegrityError:
            return HttpResponse(status=400, reason='Bad Request', content='Author already exists')
        return JsonResponse(model_to_dict(author), status=201)


@csrf_exempt
def author_detail(request, author_id):

    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return HttpResponse(status=404, reason='Not Found', content='Author does not exist')
    if request.method == 'GET':
        return JsonResponse(model_to_dict(author))
    elif request.method == 'PUT':
        data = request.POST
        author.name = data['name']
        author.save()
        return JsonResponse(model_to_dict(author))
    elif request.method == 'DELETE':
        author.delete()
        return HttpResponse(status=204)


@csrf_exempt
def author_book_list(request, author_id):
    if request.method == 'GET':
        author = Author.objects.get(pk=author_id)
        books = author.book_set.all()
        books_json = [model_to_dict(book) for book in books]
        return JsonResponse(books_json, safe=False)
    elif request.method == 'POST':
        data = request.POST
        author = Author.objects.get(pk=author_id)
        book = author.book_set.create(
            title=data['title'],
            price=data['price'],
        )
        return JsonResponse(model_to_dict(book), status=201)


@csrf_exempt
def author_book_detail(request, author_id, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponse(status=404, reason='Not Found', content='Book does not exist')
    if request.method == 'GET':
        return JsonResponse(model_to_dict(book))
    elif request.method == 'PUT':
        data = request.POST
        book.title = data['title']
        book.price = data['price']
        book.save()
        return JsonResponse(model_to_dict(book))
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)


@csrf_exempt
def author_review_list(request, author_id):
    if request.method == 'GET':
        author = Author.objects.get(pk=author_id)
        reviews = author.review_set.all()
        reviews_json = [model_to_dict(review) for review in reviews]
        return JsonResponse(reviews_json, safe=False)
    elif request.method == 'POST':
        data = request.POST
        author = Author.objects.get(pk=author_id)
        review = author.review_set.create(
            reviewer=data['reviewer'],
            comment=data['comment'],
        )
        return JsonResponse(model_to_dict(review), status=201)


@csrf_exempt
def author_review_detail(request, author_id, review_id):

    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        return HttpResponse(status=404, reason='Not Found', content='Review does not exist')
    if request.method == 'GET':
        return JsonResponse(model_to_dict(review))
    elif request.method == 'PUT':
        data = request.POST
        review.reviewer = data['reviewer']
        review.comment = data['comment']
        review.save()
        return JsonResponse(model_to_dict(review))
    elif request.method == 'DELETE':
        review.delete()
        return HttpResponse(status=204)
