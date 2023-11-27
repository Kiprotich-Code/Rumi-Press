from django.shortcuts import render, redirect
from django.views import generic
from .models import Authors
from .forms import AddAuthorForm

# Create your views here.
def index(request):
    return render(request, 'base.html', {})

def home(request):
    return render(request, 'main/dashboard.html')

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
