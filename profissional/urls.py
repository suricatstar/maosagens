from django.urls import path
from .views import CadastraProfissionalView, cadastraEspecialidadeView

urlpatterns = [
    path('cadastra_profissional/', CadastraProfissionalView.as_view(), name='cadastra_profissional'),
     path('cadastra_especialidade/', cadastraEspecialidadeView.as_view(), name='cadastra_especialidade')
    
]
