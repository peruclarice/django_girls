from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'supplier_price', 'selling_price', 'quantity')
        widgets = {
                'name': forms.TextInput(attrs={
                }),
                'description': forms.Textarea(attrs={
                }),
                'supplier_price': forms.TextInput(attrs={
                }),
                'selling_price': forms.TextInput(attrs={
                }),
                'quantity': forms.TextInput(attrs={
                })
            }
