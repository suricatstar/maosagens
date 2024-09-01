from django import forms
from .models import Especialidade


class ProfissionalForm(forms.Form):
    
    nome = forms.CharField(max_length=30,label="Nome",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome...'}))
    
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}))
    
    
    especialidade = forms.ModelMultipleChoiceField(queryset=Especialidade.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={
        'class': 'form-check d-flex flex-row flex-wrap gap-2',
    }))
    
    telefone = forms.CharField(label="Telefone", required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número...'}))
    
    