from django.forms import ModelForm
from .models import *
from django import forms

# Create your forms here
class AddAuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'

class AddBookForm(ModelForm):
    authors = forms.ModelMultipleChoiceField(
            queryset = Authors.objects.all(),
            widget = forms.CheckboxSelectMultiple
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

class AddPublisher(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class AddCategory(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'