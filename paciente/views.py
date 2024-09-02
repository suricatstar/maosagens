from django.shortcuts import redirect, render
from django.http import HttpResponse
from hashlib import sha256

from paciente.models import Paciente
from registros.models import Registradores

# Create your views here.
def Cadastro(request):
    if request.session.get('paciente'):
        return redirect('/agenda/opcoes_agenda/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html',{'status': status})

def Login(request):
    if request.session.get('paciente'):
        return redirect('/agenda/opcoes_agenda/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == "POST":
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
                nome = nome,
                email = email,
                senha = senha,
            )
            
            paciente.save()
            
            return redirect('/paciente/cadastrar_paciente/?status=0')
        except:
            return redirect('/paciente/cadastrar_paciente/?status=5')
        
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    registradores = Registradores.objects.filter(email=email)
    if registradores:
        return redirect('/registros/ver_registros/')
    
    senha = sha256(senha.encode()).hexdigest()
    
    paciente = Paciente.objects.filter(email = email).filter(senha = senha)
    
    if len(paciente) == 0:
        return redirect('/paciente/login_paciente/?status=1')
    
    elif len(paciente) > 0:
        request.session['paciente'] = paciente[0].id
        
        return redirect('/agenda/opcoes_agenda/')

def sair(request):
    request.session.flush()
    return redirect('/paciente/login_paciente/')