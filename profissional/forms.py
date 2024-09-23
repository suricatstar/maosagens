from django import forms
from .models import Especialidade


class ProfissionalForm(forms.Form):
    
    nome = forms.CharField(max_length=30,label="Nome",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome...'}))
    
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}))

    
    especialidade = forms.ModelChoiceField(queryset=Especialidade.objects.all(),label="Especilidade", widget=forms.Select(attrs={
        'class': 'form-control d-flex flex-row flex-wrap gap-2',
    }))
    
    telefone = forms.CharField(label="Telefone", required=False,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número...'}))
    
class EspecialidadeForm(forms.Form):
    especialidade = forms.CharField(max_length=60,label="Especialidade",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especialidade...'}))