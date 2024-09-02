from datetime import date
from django.http import HttpResponse
from django.shortcuts import redirect, render

from agenda.forms import AgendamentoForm
from agenda.models import Agendamento
from paciente.models import Paciente
from profissional.models import Profissional

# Create your views here.
def agenda(request):
    if request.session.get('paciente'):
        return render(request, 'opcoes_agenda.html')
    else:
        return redirect('/paciente/login_paciente/')
    
    
def ver_agenda(request):
    if request.session.get('paciente'):
        paciente_id = request.session.get('paciente')
        paciente = Paciente.objects.get(id=paciente_id)
        
        agendamentos = Agendamento.objects.filter(paciente=paciente)
        
        return render(request, 'ver_agenda.html', {'agendamentos': agendamentos})
    else:
        return redirect('/paciente/login_paciente/')
    
def valida_agenda(request): 
    if request.method == 'GET':
        form = AgendamentoForm()
        
        status = request.GET.get('status')
        return render(request, 'agendar_fiso.html', {'form': form, 'status': status})
    
    elif request.method == "POST":
        form = AgendamentoForm(request.POST)
        
        
        if form.is_valid():
            data = form.cleaned_data['data']
            hora = form.cleaned_data['hora']
            especialidade = form.cleaned_data['especialidade']
            
            paciente_id = request.session.get('paciente')
            paciente = Paciente.objects.get(id=paciente_id)
            
            profissionais = Profissional.objects.filter(area_especializacao=especialidade)
            
            profissional_disponivel = profissionais.exclude(
                agendamento__data=data,
                agendamento__hora=hora
            ).first()
            
            if data < date.today():
                return redirect('/agenda/valida_agenda/?status=1')
            
            if data.weekday() in [5,6]:
                return redirect('/agenda/valida_agenda/?status=2')
            
            if not profissional_disponivel:
                return redirect('/agenda/valida_agenda/?status=3')
            
            try:
                agendamento = Agendamento(
                    paciente=paciente,
                    profissional=profissional_disponivel,
                    especialidade=especialidade,
                    data=data,
                    hora=hora
                )
                agendamento.save()
            
                print("Hora recebida:", hora)
                print("Hora salva no modelo:", agendamento.hora)


                return redirect('/agenda/valida_agenda/?status=0')
            except:
                return redirect('/agenda/valida_agenda/?status=4')    
        
             


   # lembra de fazer a parte de anotações, creio que deva ser feito na parte de profissional.  