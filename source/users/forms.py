from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from . models import Profile

# Create your forms here
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_names', 'role', ]
