from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')

        # users = User.objects.filter(username=username)

        # if users.exists():
            
        #     return redirect('/usuarios/cadastro')


        # verifica se as senhas conferem
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, "As senhas devem ser iguais")
            return redirect('/usuarios/cadastro')

        # Verifica se a senha contem mais de 6 caracteres
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, "As senhas devem ter mais de 6 digitos")
            return redirect('/usuarios/cadastro')

        # Realiza uma consulta no banco, com o filtro sendo,
        # O usuario digitado existe no campo usuario?
        # se existir ele retorna True  
        users = User.objects.filter(username=username)

        # Verifica se o retorno da consulta do usuario é True
        # se for True ele retorna para pagina de cadastro informando isso
        if users.exists():
            messages.add_message(request, constants.ERROR, "Esse usuário ja existe")
            return redirect('/usuarios/cadastro')
        
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            return redirect('/usuarios/login')
        except:
            print('Erro 4')
            return redirect('/usuarios/cadastro')        