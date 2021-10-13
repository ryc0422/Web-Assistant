from django.db import models
from django.forms import ModelForm, TextInput, Select, NumberInput, widgets
from expenses.models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'item' : TextInput(attrs={'class':'form-control'}),
            'category' : Select(attrs={'class':'form-control'}),
            'amount' : NumberInput(attrs={'class':'form-control'}),

        }
