from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.core.paginator import Paginator
from .models import Profissional, Especialidade
from .forms import ProfissionalForm, EspecialidadeForm


# Create your views here.
class CadastraProfissionalView(FormView):
    template_name = 'cadastroProfissa.html'
    form_class = ProfissionalForm
    success_url = reverse_lazy('cadastra_profissional') 

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        status = self.request.GET.get('status')
        if status:
            context['status'] = status
        return context

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        especialidades = form.cleaned_data['especialidade']
        telefone = form.cleaned_data['telefone']

        profissional_existente = Profissional.objects.filter(nome=nome, area_especializacao=especialidades).first()

        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect('/profissional/cadastra_profissional/?status=1')

        if profissional_existente:
            return redirect('/profissional/cadastra_profissional/?status=2')

        if len(telefone) < 10:
            return redirect('/profissional/cadastra_profissional/?status=3')

        try:
            profissional = Profissional(
                nome=nome,
                email=email,
                area_especializacao=especialidades,
                telefone=telefone
            )
            profissional.save()
            return redirect('/profissional/cadastra_profissional/?status=0')

        except Exception as e:
            print(e)
            return redirect('/profissional/cadastra_profissional/?status=4')

class cadastraEspecialidadeView(FormView):
    template_name = 'cadastraEspecia.html'
    form_class = EspecialidadeForm           
    success_url = reverse_lazy('cadastra_profissional')             
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.request.GET.get('status')
        if status:
            context['status'] = status
        return context
    
    def form_valid(self, form):
        especialidade = form.cleaned_data['especialidade']

        especialidade_existente = Especialidade.objects.filter(especialidade=especialidade).first()

        if len(especialidade.strip()) == 0:
            return redirect('/profissional/cadastra_especialidade/?status=1')

        if especialidade_existente:
            return redirect('/profissional/cadastra_especialidade/?status=2')

        try:
            especialidade = Especialidade(
                especialidade=especialidade
            )
            especialidade.save()
            return redirect('/profissional/cadastra_especialidade/?status=0')

        except Exception as e:
            print(e)
            return redirect('/profissional/cadastra_especialidade/?status=3')