from django.shortcuts import render
from django.http import HttpResponse

from profissional.forms import ProfissionalForm

# Create your views here.
def cadastra_profissional(request):
    pass

def valida_profissional(request):
    if request.method == "GET":
        form = ProfissionalForm()
        return render(request, 'cadastroProfissa.html', {'form': form })
    elif request.method == "POST":
        form = ProfissionalForm(request.POST)
        
        # terminar de salvar o profissional
        return HttpResponse(form)
        