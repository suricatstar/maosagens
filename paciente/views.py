from django.shortcuts import redirect, render
from django.http import HttpResponse
from hashlib import sha256

from django.views import View

from paciente.models import Paciente
from registros.models import Registradores

# Create your views here.
class CadastroView(View):
    def get(self, request):
        if request.session.get('paciente'):
            return redirect('/agenda/opcoes_agenda/')
        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status': status})

class LoginView(View):
    def get(self, request):
        if request.session.get('paciente'):
            return redirect('/agenda/opcoes_agenda/')
        status = request.GET.get('status')
        return render(request, 'login.html', {'status': status})

class ValidaCadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')

    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')
        
        paciente = Paciente.objects.filter(email=email)
        
        if len(nome.strip()) == 0 or len(email.strip()) == 0:
            return redirect('/paciente/cadastrar_paciente/?status=1')
        
        if len(senha) < 8:
            return redirect('/paciente/cadastrar_paciente/?status=2')
        
        if senha != confirma_senha:
            return redirect('/paciente/cadastrar_paciente/?status=3')
        
        if len(paciente) > 0:
            return redirect('/paciente/cadastrar_paciente/?status=4')
        
        try:
            senha = sha256(senha.encode()).hexdigest()
            
            paciente = Paciente(
                nome=nome,
                email=email,
                senha=senha,
            )
            
            paciente.save()
            
            return redirect('/paciente/cadastrar_paciente/?status=0')
        except:
            return redirect('/paciente/cadastrar_paciente/?status=5')
        
        
class ValidaLoginView(View):
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        registradores = Registradores.objects.filter(email=email)
        if registradores:
            return redirect('/registros/ver_registros/')
        
        senha = sha256(senha.encode()).hexdigest()
        
        paciente = Paciente.objects.filter(email=email).filter(senha=senha)
        
        if len(paciente) == 0:
            return redirect('/paciente/login_paciente/?status=1')
        
        elif len(paciente) > 0:
            request.session['paciente'] = paciente[0].id
            return redirect('/agenda/opcoes_agenda/')

class SairView(View):
    def get(self, request):
        request.session.flush()
        return redirect('/paciente/login_paciente/')

# fazer com que o cliente cancele as consultas e justifique