from django.shortcuts import render
from django.views import generic
from .models import Authors

# Create your views here.
def home(request):
    return render(request, 'base.html', {})


class AuthorsListView(generic.ListView):
    model = Authors
    context_object_name = 'authors'
    template_name = 'main/authors.html'


class AuthorsDetailView(generic.DetailView):
    model = Authors
    template_name = 'main/author_details.html'
    context_object_name = 'author'

