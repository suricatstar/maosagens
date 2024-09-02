from django import forms

from profissional.models import  Especialidade

class AgendamentoForm(forms.Form):
    HORARIOS = (
        ("1", "07:00 às 08:00"),
        ("2", "08:00 às 09:00"),
        ("3", "09:00 às 10:00"),
        ("4", "10:00 às 11:00"),
        ("5", "11:00 às 12:00"),
    )
    
    paciente = forms.HiddenInput()
    profissional = forms.HiddenInput()
    especialidade = forms.ModelChoiceField(queryset=Especialidade.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    hora = forms.ChoiceField(choices=HORARIOS,widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    