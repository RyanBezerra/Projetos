from django.shortcuts import render
from django.http import HttpResponse
#from .forms import DadosForm
from .models import Dados

# Create your views here.

def Banco(request):
    return render(request, template_name='BancoDeDados/Banco.html')

def CriarBanco(request):
    #form = DadosForm()
    return render(request, template_name='BancoDeDados/CriarBanco.html')
