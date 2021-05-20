from django import forms

from app.models import Cadastro


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
