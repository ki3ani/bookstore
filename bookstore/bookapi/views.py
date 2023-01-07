from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
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



