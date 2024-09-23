from django.urls import path

from agenda.views import AgendaView, ValidaAgendaView, VerAgendaView


urlpatterns = [
    path('opcoes_agenda/', AgendaView.as_view(), name="agenda"),
    path('valida_agenda/', ValidaAgendaView.as_view(), name="valida_agenda"),
    path('ver_agenda/', VerAgendaView.as_view(), name="ver_agenda"),
]
