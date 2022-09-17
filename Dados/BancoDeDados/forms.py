#from django import forms
from django.forms import ModelForm
from .models import Dados

class DadosForm(ModelForm):

    class Meta:
        model = Dados
        fields = ['Nome', 'Valor']


