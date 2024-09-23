from django.urls import path
from .views import CadastroView, LoginView, ValidaCadastroView, ValidaLoginView, SairView

urlpatterns = [
    path('cadastrar_paciente/', CadastroView.as_view(), name='cadastrar_paciente'),
    path('login_paciente/', LoginView.as_view(), name='login_paciente'),
    path('valida_cadastro/', ValidaCadastroView.as_view(), name='valida_cadastro'),
    path('valida_login/', ValidaLoginView.as_view(), name='valida_login'),
    path('sair/', SairView.as_view(), name='sair'),
]
