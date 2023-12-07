from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    # Urls for authors
    path('authors/', login_required(views.AuthorsListView.as_view()), name='authors'),
    path('author_details/<int:pk>', login_required(views.AuthorsDetailView.as_view()), name='author_details'),
    path('add_authors/', views.add_authors, name='add_authors'),
    path('delete_author/<author_id>', views.delete_author, name='delete_author'),
    path('update_author/<author_id>', views.update_author, name='update_author'),

    # Urls for books
    path('books/', login_required(views.BooksListView.as_view()), name='books'),
    path('book_details/<int:pk>', login_required(views.BooksDetailView.as_view()), name='book_details'),
    path('add_books/', views.add_books, name='add_books'),
    path('delete_book/<book_id>', views.delete_book, name='delete_book'),
    path('update_book/<book_id>', views.update_book, name='update_book'),

    # Urls for expenses 
    path('expenses/', login_required(views.ExpenseListView.as_view()), name='expenses'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('delete_expense/<expense_id>', views.delete_expense, name='delete_expense'),
    path('update_expense/<expense_id>', views.update_expense, name='update_expense'),

    # Urls for publishers
    path('publishers/', login_required(views.PublisherListView.as_view()), name='publishers'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('delete_publisher/<pub_id>', views.delete_publisher, name='delete_publisher'),
    path('update_publisher/<pub_id>', views.update_publisher, name='update_publisher'),

    # Urls for category
    path('categories/', login_required(views.CategoryListView.as_view()), name='categories'),
    path('add_category/', views.add_category, name='add_category'),
    path('update_category/<id>', views.update_category, name='update_category'),   
]