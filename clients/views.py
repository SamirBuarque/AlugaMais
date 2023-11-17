from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    # Verificando se o usuario esta logado:
    # POST == enviando dados, ou seja, enviou o formulario.
    if request.method == 'POST':
        username = request.POST['username'] # username é o nome do input lá do formulario
        password = request.POST['password']

        #AUTENTICANDO (admin / admin@123) -> usuario django
        user = authenticate(request, username=username, password=password) # CASO A AUTENTICAÇÃO SEJA FEITA, É RETORNADO UM USER OBJECT

        if user is not None:
            login(request, user)
            messages.success(request, 'Login feito com sucesso!')
            return render(request, 'global/home.html', {})
        
        else:
            messages.error(request, 'Houve uma falha na autenticação. Tente novamente.')
            return render(request, 'clients/pages/login_user.html', {})

    else:
        return render(request, 'clients/pages/login_user.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logout feito com sucesso!')
    return render(request, 'global/home.html')


def register_user(request):
    return render(request, 'clients/pages/register_user.html')
