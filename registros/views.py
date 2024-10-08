from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from agenda.models import Agendamento
from paciente.models import Paciente
from profissional.models import Profissional

class VerRegistrosView(View):
    def get(self, request):
        return render(request, 'registro.html')

class VerPacienteView(ListView):
    paginate_by = 6
    model = Paciente
    template_name = 'ver_pacientes.html'
    context_object_name = 'pacientes'

class VerProfissionaisView(ListView):
    paginate_by = 6
    model = Profissional
    template_name = 'ver_profissionais.html'
    context_object_name = 'profissionais'

class VerAgendamentosView(ListView):
    paginate_by = 6
    model = Agendamento
    template_name = 'ver_agendamentos.html'
    context_object_name = 'agendamentos'
