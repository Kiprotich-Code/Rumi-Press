from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorsListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorsDetailView.as_view(), name='author_details'),
]