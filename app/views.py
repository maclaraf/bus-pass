from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from app.forms import CadastroForm


def pass_index(request):
    return render(request, 'app/index.html', {})


def pass_cad(request):
    contexto = {}
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['form'] = form
        form_user = UserCreationForm()
        contexto['form_user'] = form_user
        return render(request, 'app/senha.html', contexto)
    contexto['form'] = form
    return render(request, 'app/cadastrar.html', contexto)


def criar_usuario(request):
    contexto = {}
    form = UserCreationForm(request.POST or None)
    if form:
        # form.save()
        usuario = form.data['username']
        senha = form.data['password1']
        # # Create user and save to the database
        user = User.objects.create_user(usuario, '', senha)
        # # Update fields and then save again
        # user.first_name = 'John'
        # user.last_name = 'Citizen'
        user.save()
        return HttpResponseRedirect('app/index.html')
    contexto['form'] = form
    return render(request, 'app/cadastrar.html', contexto)
