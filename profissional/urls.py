from django.urls import path
from . import views

urlpatterns = [
    path('valida_profissional/', views.valida_profissional, name='valida_profissional'),
    path('cadastra_profissional/', views.cadastra_profissional, name='cadastra_profissional'),
]
