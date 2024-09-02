from django.urls import path
from . import views

urlpatterns = [
    path('opcoes_agenda/', views.agenda, name="agenda"),
    path('valida_agenda/', views.valida_agenda, name="valida_agenda"),
    path('ver_agenda/', views.ver_agenda, name="ver_agenda"),
]
