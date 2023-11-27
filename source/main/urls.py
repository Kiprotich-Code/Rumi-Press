from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('authors/', views.AuthorsListView.as_view(), name='authors'),
    path('author_details/<int:pk>', views.AuthorsDetailView.as_view(), name='author_details'),
    path('add_authors/', views.add_authors, name='add_authors'),
    path('delete_author/<author_id>', views.delete_author, name='delete_author'),
    path('update_author/<author_id>', views.update_author, name='update_author'),
]