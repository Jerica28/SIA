from django import forms
from .models import Food


class FoodForm(forms.ModelForm):

    class Meta:
        model = Food

        fields = [
            'name',
            'category',
            'price',
            'availability_status',
            'description',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter food name',
            }),

            'category': forms.Select(attrs={
                'class': 'form-control',
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'min': '0',
                'step': '0.01',
            }),

            'availability_status': forms.Select(
                choices=[
                    ('True', 'Available'),
                    ('False', 'Out of Stock'),
                ],
                attrs={'class': 'form-control'},
            ),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter food description',
                'rows': 3,
            }),
        }