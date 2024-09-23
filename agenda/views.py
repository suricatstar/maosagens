from datetime import date
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from agenda.forms import AgendamentoForm
from agenda.models import Agendamento
from paciente.models import Paciente
from profissional.models import Profissional


class AgendaView(TemplateView):
    template_name = 'opcoes_agenda.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('paciente'):
            return redirect('/paciente/login_paciente/')
        return super().dispatch(request, *args, **kwargs)


class VerAgendaView(TemplateView):
    template_name = 'ver_agenda.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('paciente'):
            return redirect('/paciente/login_paciente/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.request.session.get('paciente')
        paciente = Paciente.objects.get(id=paciente_id)
        agendamentos = Agendamento.objects.filter(paciente=paciente)
        context['agendamentos'] = agendamentos
        return context


class ValidaAgendaView(FormView):
    template_name = 'agendar_fiso.html'
    form_class = AgendamentoForm
    success_url = reverse_lazy('valida_agenda')  # Substitua pela URL adequada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.request.GET.get('status')
        if status:
            context['status'] = status
        return context

    def form_valid(self, form):
        data = form.cleaned_data['data']
        hora = form.cleaned_data['hora']
        especialidade = form.cleaned_data['especialidade']

        paciente_id = self.request.session.get('paciente')
        paciente = Paciente.objects.get(id=paciente_id)

        profissionais = Profissional.objects.filter(area_especializacao=especialidade)

        profissional_disponivel = profissionais.exclude(
            agendamento__data=data,
            agendamento__hora=hora
        ).first()

        if data < date.today():
            return redirect('/agenda/valida_agenda/?status=1')

        if data.weekday() in [5, 6]:  # Fins de semana
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

            return redirect('/agenda/valida_agenda/?status=0')

        except Exception as e:
            print(e)
            return redirect('/agenda/valida_agenda/?status=4')
