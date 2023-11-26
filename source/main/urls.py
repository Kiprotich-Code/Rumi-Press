from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorsListView.as_view(), name='authors'),
]