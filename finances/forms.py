from django import forms
from .models import Category, Transaction


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']
        widgets = {
            'type': forms.Select(choices=[('income', 'Income'), ('expense', 'Expense')]),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'description', 'category', 'transaction_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'transaction_type': forms.Select(choices=[('income', 'Income'), ('expense', 'Expense')]),
        }