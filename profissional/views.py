from django.shortcuts import render, redirect
from .models import Profissional, Especialidade
from django.http import HttpResponse

from profissional.forms import ProfissionalForm

# Create your views here.
def cadastra_profissional(request):
    if request.method == "GET":
        form = ProfissionalForm()
        
        status = request.GET.get('status')
        return render(request, 'cadastroProfissa.html', {'form': form, 'status': status})

def valida_profissional(request):
    if request.method == "GET":
        return redirect('/profissional/cadastra_profissional')
    
    elif request.method == "POST":
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            especialidades = form.cleaned_data['especialidade']
            telefone = form.cleaned_data['telefone']
            
            
            profissional_existente = Profissional.objects.filter(nome=nome).first()
            
            
            if len(nome.strip()) == 0 or len(email.strip()) == 0:
                return redirect('/profissional/cadastra_profissional/?status=1')
            
            if profissional_existente:
                
                especialidades_existentes = profissional_existente.area_especializacao.all()
                
                ids_existentes = set(especialidade.id for especialidade in especialidades_existentes)
                ids_selecionadas = set(especialidade.id for especialidade in especialidades)
                
                
                if ids_existentes.intersection(ids_selecionadas):
                    return redirect('/profissional/cadastra_profissional/?status=2')
            
            if len(telefone) < 10:
                return redirect('/profissional/cadastra_profissional/?status=3')
            
            try:
                profissional = Profissional(
                    nome= nome,
                    email = email,
                    telefone = telefone
                )
                
                profissional.save()
                
                
                profissional.area_especializacao.set(especialidades)
                
                return redirect('/profissional/cadastra_profissional/?status=0')
            
            except:
                return redirect('/profissional/cadastra_profissional/?status=4')
                
                
        