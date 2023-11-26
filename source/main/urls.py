from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('authors/', views.AuthorsListView.as_view(), name='authors'),
    path('author_details/<int:pk>', views.AuthorsDetailView.as_view(), name='author_details'),
]