from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:book_id>/', views.book_detail), 
    path('books/<int:book_id>/reviews/', views.review_list),
    path('books/<int:book_id>/reviews/<int:review_id>/', views.review_detail),
    path('authors/', views.author_list),
    path('authors/<int:author_id>/', views.author_detail),
    path('authors/<int:author_id>/books/', views.author_book_list),
    path('authors/<int:author_id>/books/<int:book_id>/', views.author_book_detail),

]