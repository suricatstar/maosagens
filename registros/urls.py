from django.urls import path
from . import views


urlpatterns = [
    path('ver_registros/', views.VerRegistrosView.as_view(), name='ver_registros'),
    path('ver_pacientes/', views.VerPacienteView.as_view(), name='ver_paciente'),
    path('ver_profissionais/', views.VerProfissionaisView.as_view(), name='ver_profissionais'),
    path('ver_agendamentos/', views.VerAgendamentosView.as_view(), name='ver_agendamentos'),
]