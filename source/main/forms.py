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


class AddExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

class AddPublisher(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'