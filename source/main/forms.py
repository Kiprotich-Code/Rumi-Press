from django.forms import ModelForm
from .models import *
from django import forms

# Create your forms here
class AddAuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Authors Name'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Authors Country of Origin'}),
            'date_born': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Authors Date of Birth'}),
            'interests': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Authors Interests(Separated With a Comma)'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Authors Biography'}),
        }

class AddBookForm(ModelForm):
    authors = Authors.objects.all()
    authors = forms.ModelMultipleChoiceField(
            queryset = Authors.objects.all(),
            widget = forms.SelectMultiple
        )

    category = forms.ModelMultipleChoiceField(
            queryset = Category.objects.all(),
            widget = forms.CheckboxSelectMultiple
        )
    class Meta:
        model = Books
        fields = '__all__'

        widgets = {
            'book_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book ID'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Subtitle'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Publisher'}),         
            'published_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Date it Was Published'})         
        }

class AddExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'book': forms.TextInput(attrs={'class': 'form-control'}),
            'distribution_date': forms.TextInput(attrs={'class': 'form-control'}),
            'distribution_expense': forms.TextInput(attrs={'class': 'form-control'}),
            'confirmed_by': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddPublisher(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
        widgets = {
            'pub_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control'}),
        }