from django.http import HttpResponse
from django.shortcuts import render

from agenda.models import Agendamento
from paciente.models import Paciente
from profissional.models import Profissional

# Create your views here.
def ver_registros(request):
    if request.method == "GET":
        return render(request,'registro.html')


def ver_paciente(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        return render(request,'ver_pacientes.html', {'pacientes' : pacientes})


def ver_profissionais(request):
    if request.method == "GET":
        profissionais = Profissional.objects.all()
        return render(request,'ver_profissionais.html', {'profissionais' : profissionais})


def ver_agendamentos(request):
    if request.method == "GET":
        agendamentos = Agendamento.objects.all()
        return render(request,'ver_agendamentos.html', {'agendamentos' : agendamentos})