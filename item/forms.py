from django import forms 
from .models import Item

# Define the full set of Tailwind classes for dark theme styling
INPUT_CLASSES = 'w-full py-3 px-4 rounded-lg border-2 border-gray-600 focus:outline-none focus:border-teal-400 bg-gray-700 text-white placeholder-gray-400'

class NewItemForm(forms.ModelForm):
    class Meta:
        model= Item
        # Corrected fields list (no 'price')
        fields = ('name','category','image','description','ingredient','process',)

        widgets= {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Name of the dish'
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                # File input needs slight adjustment to look good on a dark background
                'class': INPUT_CLASSES.replace('text-white', 'text-gray-400').replace('bg-gray-700', 'bg-gray-800') + ' py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-24', # Added height class for Textarea
                'placeholder': 'A short description or introduction to the recipe'
            }),
            'ingredient': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-32', # Added height class for Textarea
                'placeholder': 'List ingredients, one item per line'
            }),
            'process': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-48', # Added height class for Textarea
                'placeholder': 'Step-by-step instructions for the recipe'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model= Item
        # Corrected fields list (no 'category' or 'price')
        # NOTE: If you exclude 'category' in Edit, ensure it's not strictly required in the model.
        fields = ('name','image','description','ingredient','process',)

        widgets= {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Name of the dish'
            }),
            'image': forms.FileInput(attrs={
                # File input needs slight adjustment to look good on a dark background
                'class': INPUT_CLASSES.replace('text-white', 'text-gray-400').replace('bg-gray-700', 'bg-gray-800') + ' py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-24',
                'placeholder': 'A short description or introduction to the recipe'
            }),
            'ingredient': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-32',
                'placeholder': 'List ingredients, one item per line'
            }),
            'process': forms.Textarea(attrs={
                'class': INPUT_CLASSES + ' h-48',
                'placeholder': 'Step-by-step instructions for the recipe'
            })
        }