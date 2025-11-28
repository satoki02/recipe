from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Define the common set of Tailwind classes for all input fields with the new color scheme
INPUT_CLASSES = 'w-full py-3 px-4 rounded-lg border-2 border-gray-600 focus:outline-none focus:border-teal-400 bg-gray-700 text-white placeholder-gray-400'
# Changes:
# - border-2 border-gray-600: Softer border
# - bg-gray-700: Lighter input background
# - text-white: Input text remains white
# - placeholder-gray-400: Softer placeholder color

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': INPUT_CLASSES
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email Address',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': INPUT_CLASSES
    }))