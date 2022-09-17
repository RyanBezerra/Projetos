from django.shortcuts import render, redirect
from .models import Dados
from .forms import DadosForm

# Create your views here.
def home(request):
    dados = Dados.objects.all()
    data={}
    data['dados'] = dados
    return render(request, 'BancoDeDados/home.html', data)

def create(request):
    form = DadosForm(request.POST or None)
    data={}
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'BancoDeDados/create.html', data)

def leiturabanco(request, pk):
    dado = Dados.objects.get(pk=pk)
    data={}
    data['dado'] = dado

    return render(request, 'BancoDeDados/dado.html',)

def update(request, pk):
    dado = Dados.objects.get(pk=pk)
    form = DadosForm(request.POST or None, instance=dado)
    data = {}
    data['dado'] = dado
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, 'BancoDeDados/update.html', data)
    
def delete(request, pk):
    dado = Dados.objects.get(pk=pk)
    dado.delete()
    return redirect('home')
