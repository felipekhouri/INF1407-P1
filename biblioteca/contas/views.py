from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import SignUpForm


class CustomLoginView(LoginView):
    template_name = 'contas/login.html'
    redirect_authenticated_user = True


def signup(request):
    """Registro de novo usuário"""
    if request.user.is_authenticated:
        return redirect('catalogo:home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Bem-vindo(a), {user.username}! Sua conta foi criada com sucesso.')
            return redirect('catalogo:home')
    else:
        form = SignUpForm()

    return render(request, 'contas/signup.html', {'form': form})


def logout_view(request):
    """Logout do usuário"""
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('contas:login')
