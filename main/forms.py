from django import forms
from .models import Category

class BookFilterForm(forms.Form):
    min_price = forms.DecimalField(max_digits=20, decimal_places=1)
    max_price = forms.DecimalField(max_digits=20, decimal_places=1)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="All Categories"
    )