from django.forms import ModelForm
from .models import Authors

# Create your forms here
class AddAuthorForm(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'