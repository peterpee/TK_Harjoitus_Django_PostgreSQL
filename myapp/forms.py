from django import forms
from .models import Recipe

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['ateria', 'ainekset', 'ohjeet']
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age']


