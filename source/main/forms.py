from django.forms import ModelForm
from .models import *

# Create your forms here
class AddAuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'

class AddBookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class AddExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'