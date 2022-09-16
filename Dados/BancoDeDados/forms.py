from django import forms
from .models import Dados

class DadosForm(forms.ModelForm):

    class Meta:
        model = Dados
        fields = ('Nome', 'Valor')


