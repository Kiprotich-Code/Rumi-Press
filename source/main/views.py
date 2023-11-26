from django.shortcuts import render
from django.views import generic
from .models import Authors

# Create your views here.
def home(request):
    return render(request, 'base.html', {})


class AuthorsListView(generic.ListView):
    model = Authors
    template_name = 'main/authors.html'

