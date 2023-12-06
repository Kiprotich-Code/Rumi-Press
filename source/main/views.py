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
    form = AddBookForm
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('books')
    
    context = {'form': form}
    return render(request, 'main/add_book.html', context)


def delete_book(request, book_id):
    book = Books.objects.get(pk=book_id)
    book.delete()
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


def delete_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    expense.delete()
    return redirect('expenses')


def update_expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    form = AddExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('expenses')
    
    context = {'expense': expense, 'form': form}
    return render(request, 'main/update_expense.html', context)


#-------------------------------------------------------#
#------------Views for Publisher Model------------------#
#-------------------------------------------------------#
class PublisherListView(generic.ListView):
    model = Publisher
    context_object_name = 'publishers'
    template_name = 'main/publishers.html'

def add_publisher(request):
    form = AddPublisher
    if request.method == 'POST':
        form = AddPublisher(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers')
    
    context = {'form': form}
    return render(request, 'main/add_publisher.html', context)


def delete_publisher(request, pub_id):
    publisher = Publisher.objects.get(pk=pub_id)
    publisher.delete()
    return redirect('publishers')


def update_publisher(request, pub_id):
    publisher = Publisher.objects.get(pk=pub_id)
    form = AddPublisher(request.POST or None, instance=publisher)
    if form.is_valid():
        form.save()
        return redirect('publishers')
    
    context = {'publisher': publisher, 'form': form}
    return render(request, 'main/update_publisher.html', context)


#-------------------------------------------------------#
#------------Views for Category Model-------------------#
#-------------------------------------------------------#
class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'main/categories.html'


def add_category(request):
    form = AddCategory
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    
    context = {'form': form}
    return render(request, 'main/add_category.html', context)


def update_category(request, id):
    category = Category.objects.get(pk=id)
    form = AddCategory(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('categories')
    
    context = {'category': category, 'form': form}
    return render(request, 'main/update_category.html', context)