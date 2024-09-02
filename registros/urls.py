from django.urls import path
from . import views

urlpatterns = [
    path('ver_registros/', views.ver_registros, name='ver_registros'),
    path('ver_pacientes/', views.ver_paciente, name='ver_paciente'),
    path('ver_profissionais/', views.ver_profissionais, name='ver_profissionais'),
    path('ver_agendamentos/', views.ver_agendamentos, name='ver_agendamentos'),
]
