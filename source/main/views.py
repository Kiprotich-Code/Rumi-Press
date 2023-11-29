from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'base.html', {})

def home(request):
    return render(request, 'main/dashboard.html')

#-------------------------------------------------------#
#------------Views for Authors Model--------------------#
#-------------------------------------------------------#
class AuthorsListView(generic.ListView):
    model = Authors
    context_object_name = 'authors'
    template_name = 'main/authors.html'


class AuthorsDetailView(generic.DetailView):
    model = Authors
    template_name = 'main/author_details.html'
    context_object_name = 'author'

def add_authors(request):
    form = AddAuthorForm
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    
    context = {'form': form}
    return render(request, 'main/add_authors.html', context)

def delete_author(request, author_id):
    author = Authors.objects.get(pk=author_id)
    author.delete()
    return redirect('authors')

def update_author(request, author_id):
    author = Authors.objects.get(pk=author_id)
    form = AddAuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('authors')

    return render(request, 'main/update_author.html', {'author': author, 'form': form})

#-------------------------------------------------------#
#------------Views for Books Model----------------------#
#-------------------------------------------------------#
class BooksListView(generic.ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'main/books.html'


class BooksDetailView(generic.DetailView):
    model = Books
    template_name = 'main/book_details.html'
    context_object_name = 'books'

def add_books(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        authors = request.POST['authors']
        if form.is_valid():

            form.save()
            return redirect('books')
    return render(request, 'main/add_book.html', {'form': form})


def delete_book(request, book_id):
    author = Books.objects.get(pk=book_id)
    author.delete()
    return redirect('books')

def update_book(request, book_id):
    book = Books.objects.get(pk=book_id)
    form = AddBookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books')

    return render(request, 'main/update_book.html', {'book': book, 'form': form})

#-------------------------------------------------------#
#------------Views for Expense Model--------------------#
#-------------------------------------------------------#
class ExpenseListView(generic.ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'main/expenses.html'

def add_expense(request):
    form = AddExpenseForm
    if request.method == 'POST':
        form = AddExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    
    context = {'form': form}
    return render(request, 'main/add_expense.html', context)


#-------------------------------------------------------#
#------------Views for Publisher Model------------------#
#-------------------------------------------------------#